---
url: https://docs.cloud.google.com/iam/docs/org-policy-custom-constraints/
title: Use custom organization policies for allow policies \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:58.268490+00:00
---

# Use custom organization policies for allow policies  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/org-policy-custom-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Use custom organization policies for allow policies Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to use Organization Policy Service custom constraints to restrict specific operations on the following Google Cloud resources:

  * `iam.googleapis.com/AllowPolicy`



To learn more about Organization Policy, see [Custom organization policies](https://docs.cloud.google.com/organization-policy/overview#custom-organization-policies).

## About organization policies and constraints

The Google Cloud Organization Policy Service gives you centralized, programmatic control over your organization's resources. As the [organization policy administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin), you can define an organization policy, which is a set of restrictions called _constraints_ that apply to Google Cloud resources and descendants of those resources in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). You can enforce organization policies at the organization, folder, or project level.

Organization Policy provides built-in [managed constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints) for various Google Cloud services. However, if you want more granular, customizable control over the specific fields that are restricted in your organization policies, you can also create _custom constraints_ and use those custom constraints in an organization policy.

### Policy inheritance

By default, organization policies are inherited by the descendants of the resources on which you enforce the policy. For example, if you enforce a policy on a folder, Google Cloud enforces the policy on all projects in the folder. To learn more about this behavior and how to change it, refer to [Hierarchy evaluation rules](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation#disallow_inheritance).

### Benefits

You can use custom organization policies that reference IAM attributes to control how your allow policies can be modified. Specifically, you can control the following:

  * Who can be granted roles
  * Who can have their roles revoked
  * Which roles can be granted
  * Which roles can be revoked



For example, you can prevent roles that contain the word `admin` from being granted to principals whose email addresses end in `@gmail.com`.

## Limitations

  * Custom organization policies in [dry-run mode](https://docs.cloud.google.com/resource-manager/docs/organization-policy/dry-run-policy) that reference IAM attributes have some limitations. Namely, audit logs for violations that involve the `setIamPolicy` method might be missing the following fields:

    * `resourceName`
    * `serviceName`
    * `methodName`
  * Audit logs aren't generated for all IAM-related custom organization policy violations. Namely, if a custom organization policy causes a `setIamPolicy` operation on the organization resource to fail, then Google Cloud doesn't generate an audit log for that event.

  * Custom organization policies that reference IAM attributes don't affect the following:

    * Default grants by [Cloud Storage ACLs](https://docs.cloud.google.com/storage/docs/access-control/lists#default).
    * Automatic role grants for [Cloud Storage convenience values](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#basic-roles-modifiable) and [BigQuery default dataset access](https://docs.cloud.google.com/bigquery/docs/access-control-basic-roles#dataset-basic-roles).
    * Roles granted by [default allow policies](https://docs.cloud.google.com/iam/docs/allow-policies#default)—for example, a project creator automatically being granted the Owner role (`roles/owner`) on the project.
  * Users can be sent invitations to become owners, even if you have a custom organization policy that prevents the Owner role (`roles/owner`) from being granted. However, while the custom organization policy doesn't prevent an invitation from being sent, it does prevent invited users from being granted the Owner role. If invited users try to accept the invitation, they'll encounter an error and won't be granted the Owner role.

  * Some actions in Google Cloud, such as creating resources or enabling APIs, involve automatically granting a role to a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) or [default service account](https://docs.cloud.google.com/iam/docs/service-account-types#default). If an action involves automatically granting a role and an organization policy prevents that role from being granted, then the entire operation might fail.

If you encounter this issue, you can use [tags](https://docs.cloud.google.com/resource-manager/docs/organization-policy/tags-organization-policy#setting_an_organization_policy_with_tags) to temporarily disable the constraint that prevents the role grant. Then, perform the action. After the action finishes, re-enable the constraint.




## Before you begin

  * If you want to test out custom organization policies that reference IAM resources, create a new project. Testing these organization policies in an existing project could disrupt security workflows. 

    1. In the Google Cloud console, go to the project selector page.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

    2. Select or create a Google Cloud project.

**Roles required to select or create a project**

       * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
       * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.



### Required roles

To get the permissions that you need to manage organization policies, ask your administrator to grant you the following IAM roles: 

  * [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) on the organization
  * Test the organization policies described on this page: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) on the project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage organization policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage organization policies:

  * `orgpolicy.*` on the organization
  * Test the organization policies described on this page: `resourcemanager.projects.setIamPolicy` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Identity and Access Management supported resources

IAM supports the `AllowPolicy` resource. This resource has the attribute `resources.bindings` attribute, which is returned for all methods that modify a resource's allow policy. All of the methods that modify a resource's allow policy end with `setIamPolicy`.

The `resource.bindings` attribute has the following structure, where `BINDINGS` is an array of role bindings that were modified during a change to an allow policy:
    
    
    {
      "bindings": {
        BINDINGS
      }
    }
    

Each binding in `resource.bindings` has the following structure, where `ROLE` is the name of the role in the role binding and `MEMBERS` is a list of identifiers for all principals that were added to or removed from the role binding:
    
    
    {
      "role": "ROLE"
      "members": {
        MEMBERS
      }
    }
    

To see the formats that principal identifiers can have, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

You can only evaluate the `resource.bindings` attribute and its fields using the supported functions. Other operators and functions—like `==`, `!=`, `in`, `contains`, `startsWith`, and `endsWith`—are not supported.

### Supported functions

You can use the following CEL functions to evaluate individual roles and members in a binding.

To evaluate all bindings in the `bindings` array or all members in the `members` array, use the `all` and `exists` macros. For more information, see Macros to evaluate lists on this page.

You can also use the logical operators `&&` (`and`) and `||` (`or`) to write multipart conditions.

Function | Description  
---|---  
`RoleNameMatches(  
role,  
roleNames: list  
)` trending_flat `bool` |  Returns `true` if the role `role` fully matches at least one of the roles listed in `roleNames`. 

Parameters
     `role`: the role to evaluate. 
     `roleNames`: a list of role names to match against. 
Example
     Returns `true` if the `role` in the specified `binding` is `roles/storage.admin` or `roles/compute.admin`: 
    
    
    RoleNameMatches(binding.role, ['roles/storage.admin', 'roles/compute.admin'])  
  
`RoleNameStartsWith(  
role,  
rolePrefixes: list  
)` trending_flat `bool` |  Returns `true` if the role `role` starts with at least one of the strings listed in `rolePrefixes`. 

Parameters
     `role`: the role to evaluate. 
     `rolePrefixes`: a list of strings to match the start of the role against. 
Example
     Returns `true` if the `role` in the specified `binding` starts with `roles/storage`: 
    
    
    RoleNameStartsWith(binding.role, ['roles/storage'])  
  
`RoleNameEndsWith(  
role,  
roleSuffixes: list  
)` trending_flat `bool` |  Returns `true` if the role `role` ends with at least one of the strings listed in `roleSuffixes`. 

Parameters
     `role`: the role to evaluate. 
     `roleSuffixes`: a list of strings to match the end of the role against. 
Example
     Returns `true` if the `role` in the specified `binding` ends with `.admin`: 
    
    
    RoleNameEndsWith(binding.role, ['.admin'])  
  
`RoleNameContains(  
role,  
roleSubstrings: list  
)` trending_flat `bool` |  Returns `true` if the role `role` contains at least one of the strings listed in `roleSubstrings`. 

Parameters
     `role`: the role to evaluate. 
     `roleSubstrings`: a list of strings to match any part of the role to. 
Example
     Returns `true` if the `role` in the specified `binding` contains the string `admin`: 
    
    
    RoleNameContains(binding.role, ['admin'])  
  
`MemberSubjectMatches(  
member,  
memberNames: list  
)` trending_flat `bool` |  Returns `true` if the member `member` fully matches at least one of the members listed in `memberNames`.  If the identifier for `member` is an email address, this function evaluates the email address as well as any [aliases](https://support.google.com/a/answer/33327) for that email address. 

Parameters
     `member`: the member to evaluate. 
     `memberNames`: a list of member names to match against. 
Example
     Returns `true` if the member `member` is `rosario@example.com`: 
    
    
    MemberSubjectMatches(member, ['user:rosario@example.com'])  
  
`MemberSubjectStartsWith(  
member,  
memberPrefixes: list  
)` trending_flat `bool` |  Returns `true` if the member `member` starts with at least one of the strings listed in `memberPrefixes`.  If the identifier for `member` is an email address, this function evaluates the email address as well as any [aliases](https://support.google.com/a/answer/33327) for that email address. 

Parameters
     `member`: the member to evaluate. 
     `memberPrefixes`: a list of strings to match the beginning of the member name against. 
Example
     Returns `true` if the member `member` begins with `user:prod-`: 
    
    
    MemberSubjectStartsWith(member, ['user:prod-'])  
  
`MemberSubjectEndsWith(  
member,  
memberSuffixes: list  
)` trending_flat `bool` |  Returns `true` if the member `member` ends with at least one of the strings listed in `memberSuffixes`.  If the identifier for `member` is an email address, this function evaluates the email address as well as any [aliases](https://support.google.com/a/answer/33327) for that email address. 

Parameters
     `member`: the member to evaluate. 
     `memberSuffixes`: a list of strings to match the end of the member name against. 
Example
     Returns `true` if the member `member` ends with `@example.com`: 
    
    
    MemberSubjectEndsWith(member, ['@example.com'])  
  
`MemberInPrincipalSet(  
member,  
principalSets: list  
)` trending_flat `bool` |  Returns `true` if the member belongs to at least one of the listed principal sets. 

Parameters
     `member`: the member to evaluate. 
     `principalSets`: a list of principal sets. For the function to evaluate to `true`, the member must be in at least one of these principal sets.  The only principal set that is supported is the organization principal set, which has the format `//cloudresourcemanager.googleapis.com/organizations/ORGANIZATION_ID`. When used in the `MemberInPrincipalSet` function, this principal set includes the following principals: 

  * All identities in all domains associated with your Google Workspace customer ID 
  * All workforce identity pools in your organization 
  * All service accounts and workload identity pools in any project in the organization 
  * All [service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) associated with resources in your organization. 


Example
     Returns `true` if the member `member` belongs to the `@example.com` organization, which has the ID `123456789012`: 
    
    
    MemberInPrincipalSet(member, ['//cloudresourcemanager.googleapis.com/organizations/123456789012'])  
  
`MemberTypeMatches(  
member,  
principalType: list  
)` trending_flat `bool` |  Returns `true` if the member is one of the listed principal types. 

Parameters
     `member`: the member to evaluate. 
     `principalType`: a list of principal types. For the function to evaluate to `true`, the member must be one of the listed principal types. To learn which principal types are supported, see Supported principal types for `MemberTypeMatches`. 
Example
     Returns `true` if the member `member` has the principal type `iam.googleapis.com/WorkspacePrincipal` or `iam.googleapis.com/WorkspaceGroup`: 
    
    
    MemberTypeMatches(member, ['iam.googleapis.com/WorkspacePrincipal', 'iam.googleapis.com/WorkspaceGroup'])  
  
### Macros to evaluate lists

Use the `all` and `exists` macros to evaluate a condition expression for a list of items.

Macro | Description  
---|---  
`list.``all(  
item,  
conditionExpression  
)` trending_flat `bool` |  Returns `true` if `conditionExpression` evaluates to `true` for _every_ `item` in `list`.  This macro is typically used for custom organization policies with the `actionType` `ALLOW`. For example, you can use this macro to ensure that an action is only allowed if _all_ modified principals meet the condition. 

Parameters
     `list`: the list of items to evaluate. 
     `item`: the list item to evaluate. For example, if you call this method on the list `resource.bindings`, then use the value `binding`. 
     `conditionExpression`: the condition expression to evaluate each `item` against. 
Example
     Returns `true` if all of the bindings in `resource.bindings` have roles that start with `roles/storage.`. Returns `false` if any of the bindings have roles that don't start with `roles/storage.`: 
    
    
    resource.bindings.all(binding, RoleNameStartsWith(binding.role, ['roles/storage.']))  
  
`list.``exists(  
item,  
conditionExpression  
)` trending_flat `bool` |  Returns `true` if `conditionExpression` evaluates to `true` for _any_ `item` in `list`.  This macro is typically used for custom organization policies with the `actionType` `DENY`. For example, you can use this macro to ensure that an action is denied if _any_ of the modified principals meet the condition. 

Parameters
     `list`: the list of items to evaluate. 
     `item`: the list item to evaluate. For example, if you call this method on the list `resource.bindings`, then use the value `binding`. 
     `conditionExpression`: the condition expression to evaluate each `item` against. 
Example
     Returns `true` if any of the bindings in `resource.bindings` have roles that start with `roles/storage.`. Returns `false` if none of the bindings have roles that start with `roles/storage.`: 
    
    
    resource.bindings.exists(binding, RoleNameStartsWith(binding.role, ['roles/storage.']))  
  
#### Conditions with nested lists

In general, if your condition includes nested lists, you should use the same macro for all lists in the condition.

Consider the following examples:

  * If your policy has the `actionType` `ALLOW`, then use the `all` macro for both the `members` list and the `bindings` list to ensure that policy modifications are only allowed if _all_ members in _all_ modified bindings satisfy the condition.
  * If your policy has the `actionType` `DENY`, then use the `exists` macro for both the `members` list and the `bindings` list to ensure that policy modifications aren't allowed if _any_ member in _any_ modified binding satisfies the condition.



Mixing macros in a single condition might result in a condition that doesn't behave how you intended.

For example, imagine that you want to prevent roles from being granted to members outside of the `example.com` organization. The `example.com` organization has the ID `123456789012`.

To accomplish this goal, you write the following condition:

Not recommended — misconfigured condition
    
    
    "resource.bindings.**all**(
      binding,
      binding.members.**exists**(member,
        MemberInPrincipalSet(member, ['//cloudresourcemanager.googleapis.com/organizations/123456789012'])
      )
    )"
    

This condition appears to prevent roles from being granted to members outside of the `example.com` organization. However, the condition evaluates to `true` if _any_ member in each of the modified role bindings is in the `example.com` organization. As a result, you can still grant roles to members outside of the `example.com` organization if you also grant the same role to a member in the `example.com` organization.

For example, the condition evaluates to `true` for the following set of bindings, even though one of the members isn't in the `example.com` organization:
    
    
     "bindings": [
        {
          "members": [
            "**user:raha@altostrat.com** ",
            "user:jie@example.com"
          ],
          "role": "roles/resourcemanager.projectCreator"
        }
      ],

Instead, you should write a condition like the following:

Recommended — correctly configured condition
    
    
    "resource.bindings.**all**(
      binding,
      binding.members.**all**(member,
        MemberInPrincipalSet(member, ['//cloudresourcemanager.googleapis.com/organizations/123456789012'])
      )
    )"
    

Using the `all` macro for both the `members.bindings` array and the `resource.bindings` array ensures that the condition evaluates to `true` only if _all_ members in _all_ bindings are in the `example.com` principal set.

### Supported principal types for `MemberTypeMatches`

The `MemberTypeMatches` function requires you to specify which principal type the specified member must match.

The following table lists the principal types that you can enter and a description of what the principal type represents. It also lists the principal identifiers that correspond with each principal type. These identifiers are the values that are used in IAM policies.

Principal type | Description | Principal identifiers  
---|---|---  
`iam.googleapis.com/ConsumerPrincipal` |  A [consumer Google Account](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#google_for_consumers). The email addresses for these accounts typically end in `gmail.com`.  | `user:USER_EMAIL_ADDRESS`  
`iam.googleapis.com/WorkspacePrincipal` |  A Google Account that is part of a Cloud Identity or Google Workspace account. These accounts are also called [ managed user accounts](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#managed_user_account).  | `user:USER_EMAIL_ADDRESS`  
`iam.googleapis.com/ConsumerGroup` |  A [ Google group](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#group) created by a consumer Google Account. These groups aren't owned by a Cloud Identity or Google Workspace account. The email addresses for these groups typically end in `googlegroups.com`.  | `group:GROUP_EMAIL_ADDRESS`  
`iam.googleapis.com/WorkspaceGroup` |  A [ Google group](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#group) that's owned by a Cloud Identity or Google Workspace account.  | `group:GROUP_EMAIL_ADDRESS`  
`iam.googleapis.com/Domain` |  A Cloud Identity or Google Workspace account.  | `domain:DOMAIN`  
`iam.googleapis.com/WorkforcePoolPrincipal` |  A single principal in a [workforce identity pool](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#workforce-identity-pools).  | `principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/SUBJECT_ATTRIBUTE_VALUE`  
`iam.googleapis.com/WorkforcePoolPrincipalSet` |  A principal set that contains a set of identities in a [workforce identity pool](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#workforce-identity-pools). For example, a principal set containing all principals in a workforce identity pool.  | 

  * `principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/group/GROUP_ID`
  * `principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE`
  * `principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/*`

  
`iam.googleapis.com/WorkloadPoolPrincipal` |  A single identity in a [workload identity pool](https://docs.cloud.google.com/iam/docs/workload-identity-federation#pools) | `principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT_ATTRIBUTE_VALUE`  
`iam.googleapis.com/WorkloadPoolPrincipalSet` |  A principal set that contains a set of identities in a [workload identity pool](https://docs.cloud.google.com/iam/docs/workload-identity-federation#pools). For example, a principal set containing all principals in a workload identity pool.  | 

  * `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/group/GROUP_ID`
  * `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE`
  * `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/*`

  
`iam.googleapis.com/ServiceAccount` |  Any [service account](https://docs.cloud.google.com/iam/docs/service-account-overview). A service account is a special type of account that represents a workload rather than a human user.  In the context of the `MemberTypeMatches` function, this principal type doesn't include [service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents).  | `serviceAccount:SERVICE_ACCOUNT_EMAIL_ADDRESS`  
`iam.googleapis.com/ServiceAgent` |  Any [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents). A service agent is a special type of service account that Google Cloud creates and manages. When granted roles in your projects, service agents let Google Cloud services perform actions on your behalf.  | `serviceAccount:SERVICE_AGENT_EMAIL_ADDRESS`  
`iam.googleapis.com/PublicPrincipals` |  The principals `allUsers` and `allAuthenticatedUsers`.  | 

  * `allUsers`
  * `allAuthenticatedUsers`

  
`iam.googleapis.com/ProjectRoleReference` |  Principals that are defined based on the role granted to them. These principals are also called [convenience values](https://docs.cloud.google.com/storage/docs/access-control/iam#convenience-values).  | 

  * `projectOwner:PROJECT_ID`
  * `projectEditor:PROJECT_ID`
  * `projectViewer:PROJECT_ID`

  
`iam.googleapis.com/ResourcePrincipal` |  A resource with a [built-in identity](https://docs.cloud.google.com/iam/docs/built-in-resource-identities).  |  Any of the principal identifiers listed in [Principal identifiers for single resources](https://docs.cloud.google.com/iam/docs/resources-with-built-in-identities#single-resources).   
`iam.googleapis.com/ResourcePrincipalSet` |  Resources with [built-in identities](https://docs.cloud.google.com/iam/docs/built-in-resource-identities) that share certain characteristics, such as type or ancestor.  |  Any of the identifiers listed in [Principal identifiers for sets of resources](https://docs.cloud.google.com/iam/docs/resources-with-built-in-identities#resource-sets).   
`iam.googleapis.com/AgenticIdentityPoolPrincipal` |  A single [agent identity](https://docs.cloud.google.com/iam/docs/workload-identities#agent-identity).  | 

  * `principal://agents.global.org-ORG_ID.system.id.goog/SUBJECT_ATTRIBUTE_VALUE`
  * `principal://agents.global.proj-PROJECT_NUMBER.system.id.goog/SUBJECT_ATTRIBUTE_VALUE`
  * `principal://agents-nonprod.global.org-ORG_ID.system.id.goog/SUBJECT_ATTRIBUTE_VALUE`
  * `principal://agents-nonprod.global.proj-PROJECT_NUMBER.system.id.goog/SUBJECT_ATTRIBUTE_VALUE`

  
`iam.googleapis.com/AgenticIdentityPoolPrincipalSet` |  A principal set that contains a set of [agent identities](https://docs.cloud.google.com/iam/docs/workload-identities#agent-identity).  | 

  * `principalSet://agents.global.org-ORG_ID.system.id.goog/*`
  * `principalSet://agents.global.proj-PROJECT_NUMBER.system.id.goog/*`
  * `principalSet://agents-nonprod.global.org-ORG_ID.system.id.goog/*`
  * `principalSet://agents-nonprod.global.proj-PROJECT_NUMBER.system.id.goog/*`
  * `principalSet://agents.global.org-ORG_ID.system.id.goog/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE`
  * `principalSet://agents.global.proj-PROJECT_NUMBER.system.id.goog/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE`
  * `principalSet://agents-nonprod.global.org-ORG_ID.system.id.goog/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE`
  * `principalSet://agents-nonprod.global.proj-PROJECT_NUMBER.system.id.goog/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE`

Example: `principalSet://agents.global.org-123456789012.system.id.goog/*`  
  
## Set up a custom constraint

A custom constraint is defined in a YAML file by the resources, methods, conditions, and actions that are supported by the service on which you are enforcing the organization policy. Conditions for your custom constraints are defined using [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md). For more information about how to build conditions in custom constraints using CEL, see the CEL section of [Creating and managing custom constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints#common_expression_language).

### Console

To create a custom constraint, do the following: 

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. Click add **Custom constraint**. 
  4. In the **Display name** box, enter a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use personally identifiable information (PII) or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
  5. In the **Constraint ID** box, enter the ID that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example `custom.denyProjectIAMAdmin`. This field can contain up to 70 characters, not counting the prefix (`custom.`), for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
  6. In the **Description** box, enter a human-readable description of the constraint. This description is used as an error message when the policy is violated. Include details about why the policy violation occurred and how to resolve the policy violation. Don't include PII or sensitive data in your description, because it could be exposed in error messages. This field can contain up to 2000 characters. 
  7. In the **Resource type** box, select the name of the Google Cloud REST resource containing the object and field that you want to restrict—for example, `container.googleapis.com/NodePool`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
  8. Under **Enforcement method** , select whether to enforce the constraint on a REST `CREATE` method or both `CREATE` and `UPDATE` methods. If you enforce the constraint with the `UPDATE` method on a resource that violates the constraint, changes to that resource are blocked by the organization policy unless the change resolves the violation. 

To see supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

  9. To define a condition, click edit **Edit condition**. 
     1. In the **Add condition** panel, create a CEL condition that refers to a supported service resource, for example, `resource.management.autoUpgrade == false`. This field can contain up to 1000 characters. For details about CEL usage, see [ Common Expression Language](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language). For more information about the service resources you can use in your custom constraints, see [ Custom constraint supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/custom-constraint-supported-services). 
     2. Click **Save**. 
  10. Under **Action** , select whether to allow or deny the evaluated method if the condition is met. 

The deny action means that the operation to create or update the resource is blocked if the condition evaluates to true. 

The allow action means that the operation to create or update the resource is permitted only if the condition evaluates to true. Every other case except those explicitly listed in the condition is blocked. 

  11. Click **Create constraint**. 

When you have entered a value into each field, the equivalent YAML configuration for this custom constraint appears on the right. 




### gcloud

  1. To create a custom constraint, create a YAML file using the following format: 
    
    name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
    resourceTypes: RESOURCE_NAME
    methodTypes:
      - CREATE  
      - UPDATE 
    condition: "CONDITION"
    actionType: ACTION
    displayName: DISPLAY_NAME
    description: DESCRIPTION

Replace the following: 

     * `ORGANIZATION_ID`: your organization ID, such as `123456789`. 
     * `CONSTRAINT_NAME`: the name that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example, `custom.denyProjectIAMAdmin`. This field can contain up to 70 characters, not counting the prefix (`custom.`)— for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
     * `RESOURCE_NAME`: the fully qualified name of the Google Cloud resource containing the object and field that you want to restrict. For example, `iam.googleapis.com/AllowPolicy`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
     * `methodTypes`: the REST methods that the constraint is enforced on. Can be `CREATE` or both `CREATE` and `UPDATE`. If you enforce the constraint with the `UPDATE` method on a resource that violates the constraint, changes to that resource are blocked by the organization policy unless the change resolves the violation. 

To see the supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

     * `CONDITION`: a [ CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field can contain up to 1000 characters. For example, ``resource.bindings.exists(binding, RoleNameMatches(binding.role, ['roles/resourcemanager.projectIamAdmin']))``. 

For more information about the resources available to write conditions against, see Supported resources. 

     * `ACTION`: the action to take if the `condition` is met. Possible values are `ALLOW` and `DENY`. 

The allow action means that if the condition evaluates to true, the operation to create or update the resource is permitted. This also means that every other case except the one explicitly listed in the condition is blocked. 

The deny action means that if the condition evaluates to true, the operation to create or update the resource is blocked. 

     * `DISPLAY_NAME`: a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use PII or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
     * `DESCRIPTION`: a human-friendly description of the constraint to display as an error message when the policy is violated. This field can contain up to 2000 characters. 
  2. After you have created the YAML file for a new custom constraint, you must set it up to make it available for organization policies in your organization. To set up a custom constraint, use the [ `gcloud org-policies set-custom-constraint`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-custom-constraint) command: 
    
    gcloud org-policies set-custom-constraint CONSTRAINT_PATH

Replace `CONSTRAINT_PATH` with the full path to your custom constraint file. For example, `/home/user/customconstraint.yaml`. 

After this operation is complete, your custom constraints are available as organization policies in your list of Google Cloud organization policies. 

  3. To verify that the custom constraint exists, use the [ `gcloud org-policies list-custom-constraints`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/list-custom-constraints) command: 
    
    gcloud org-policies list-custom-constraints --organization=ORGANIZATION_ID

Replace `ORGANIZATION_ID` with the ID of your organization resource. 

For more information, see [ Viewing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#viewing_organization_policies). 




## Enforce a custom organization policy

You can enforce a constraint by creating an organization policy that references it, and then applying that organization policy to a Google Cloud resource. 

### Console

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. From the list on the **Organization policies** page, select your constraint to view the **Policy details** page for that constraint. 
  4. To configure the organization policy for this resource, click **Manage policy**. 
  5. On the **Edit policy** page, select **Override parent's policy**. 
  6. Click **Add a rule**. 
  7. In the **Enforcement** section, select whether this organization policy is enforced or not. 
  8. Optional: To make the organization policy conditional on a tag, click **Add condition**. Note that if you add a conditional rule to an organization policy, you must add at least one unconditional rule or the policy cannot be saved. For more information, see [ Scope organization policies with tags](https://docs.cloud.google.com/organization-policy/scope-policies). 
  9. To enforce the organization policy in dry-run mode, click **Set dry run policy**. For more information, see [ Test organization policies](https://docs.cloud.google.com/organization-policy/test-policies). 
  10. After you verify that the organization policy in dry-run mode works as intended, set the live policy by clicking **Set policy**. 



### gcloud

  1. To create an organization policy with boolean rules, create a policy YAML file that references the constraint: 
    
    name: projects/PROJECT_ID/policies/CONSTRAINT_NAME
    spec:
      rules:
      - enforce: true
    
    dryRunSpec:
      rules:
      - enforce: true

Replace the following: 

     * `PROJECT_ID`: the project that you want to enforce your constraint on. 
     * `CONSTRAINT_NAME`: the name you defined for your custom constraint. For example, `custom.denyProjectIAMAdmin`. 
  2. To enforce the organization policy in [dry-run mode](https://docs.cloud.google.com/organization-policy/test-policies), run the following command with the `dryRunSpec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=dryRunSpec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 

  3. After you verify that the organization policy in dry-run mode works as intended, set the live policy with the `org-policies set-policy` command and the `spec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=spec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 




## Test the custom organization policy

Optionally, you can test the organization policy by setting the policy and then trying to take an action that the policy should prevent.

### Create the constraint

  1. Save the following file as `constraint-deny-project-iam-admin`.
         
         name: organizations/ORG_ID/customConstraints/custom.denyProjectIAMAdmin
         resourceTypes: iam.googleapis.com/AllowPolicy
         methodTypes:
           - CREATE
           - UPDATE
         condition:
           "resource.bindings.exists(
             binding,
             RoleNameMatches(binding.role, ['roles/resourcemanager.projectIamAdmin']) &&
             binding.members.exists(member,
               MemberSubjectMatches(member, ['user:EMAIL_ADDRESS'])
             )
           )"
         actionType: DENY
         displayName: Do not allow EMAIL_ADDRESS to be granted the Project IAM Admin role.
         

Replace the following values:

     * `ORG_ID`: the numeric ID of your Google Cloud organization.
     * `MEMBER_EMAIL_ADDRESS`: the email address of the principal that you want to use to test the custom constraint. While the constraint is active, this principal won't be able to be granted the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`) on the project that you enforce the constraint for.
  2. Apply the constraint:
         
         gcloud org-policies set-custom-constraint ~/constraint-deny-project-iam-admin.yaml
         

  3. Verify that the constraint exists:
         
         gcloud org-policies list-custom-constraints --organization=ORGANIZATION_ID
         




### Create the policy

  1. Save the following file as `policy-deny-project-iam-admin.yaml`:
         
         name: projects/PROJECT_ID/policies/custom.denyProjectIamAdmin
         spec:
           rules:
           - enforce: true
         

Replace `PROJECT_ID` with your project ID.

  2. Apply the policy:
         
         gcloud org-policies set-policy ~/policy-deny-project-iam-admin.yaml
         

  3. Verify that the policy exists:
         
         gcloud org-policies list --project=PROJECT_ID
         




After you apply the policy, wait for about two minutes for Google Cloud to start enforcing the policy.

### Test the policy

Try to grant the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`) to the principal whose email address you included in the custom constraint. Before running the command, replace the following values:

  * `PROJECT_ID`: The ID of the Google Cloud project where you enforced the constraint
  * `EMAIL_ADDRESS`: The email address of the principal that you specified when you created the organization policy constraint.


    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=user:EMAIL_ADDRESS --role=roles/resourcemanager.projectIamAdmin

The output is the following:
    
    
    Operation denied by custom org policies: ["customConstraints/custom.denyProjectIAMAdmin": "EMAIL_ADDRESS can't be granted the Project IAM Admin role."]
    

## Example custom organization policies for common use cases

The following table provides the syntax of some custom constraints for common use cases.

The following examples use the CEL macros `all` and `exists`. For more information about these macros, see Macros to evaluate lists.

Description | Constraint syntax  
---|---  
  
Block the ability to grant a specific role.  | 
    
    
    name: organizations/ORG_ID/customConstraints/custom.denyRole
    resourceTypes: iam.googleapis.com/AllowPolicy
    methodTypes:
      - CREATE
      - UPDATE
    condition:
    "resource.bindings.exists(
        binding,
        RoleNameMatches(binding.role, ['ROLE'])
      )"
    actionType: DENY
    displayName: Do not allow the ROLE role to be granted  
  
Only allow specific roles to be granted.  | 
    
    
    name: organizations/ORG_ID/customConstraints/custom.specificRolesOnly
    resourceTypes: iam.googleapis.com/AllowPolicy
    methodTypes:
      - CREATE
      - UPDATE
    condition:
      "resource.bindings.all(
        binding,
        RoleNameMatches(binding.role, ['ROLE_1', 'ROLE_2'])
      )"
    actionType: ALLOW
    displayName: Only allow the ROLE_1 role and ROLE_2 role to be granted  
  
Prevent any roles that start with `roles/storage.` from being granted.  | 
    
    
    name: organizations/ORG_ID/customConstraints/custom.dontgrantStorageRoles
    resourceTypes: iam.googleapis.com/AllowPolicy
    methodTypes:
      - CREATE
      - UPDATE
    condition:
      "resource.bindings.exists(
        binding,
        RoleNameStartsWith(binding.role, ['roles/storage.'])
      )"
    actionType: DENY
    displayName: Prevent roles that start with "roles/storage." from being granted  
  
Prevent any roles with `admin` in the name from being revoked.  | 
    
    
    name: organizations/ORG_ID/customConstraints/custom.dontRevokeAdminRoles
    resourceTypes: iam.googleapis.com/AllowPolicy
    methodTypes:
      - REMOVE_GRANT
    condition:
      "resource.bindings.exists(
        binding,
        RoleNameContains(binding.role, ['admin'])
      )"
    actionType: DENY
    displayName: Prevent roles with "admin" in their names from being revoked  
  
Only allow specific principals to be granted roles.  | 
    
    
    name: organizations/ORG_ID/customConstraints/custom.allowSpecificPrincipals
    resourceTypes: iam.googleapis.com/AllowPolicy
    methodTypes:
      - CREATE
      - UPDATE
    condition:
      "resource.bindings.all(
        binding,
        binding.members.all(member,
          MemberSubjectMatches(member, ['user:USER','serviceAccount:SERVICE_ACCOUNT'])
        )
      )"
    actionType: ALLOW
    displayName: Only allow roles to be granted to USER and SERVICE_ACCOUNT  
  
Prevent any roles from being revoked from specific principals.  | 
    
    
    name: organizations/ORG_ID/customConstraints/custom.denyRemovalOfSpecificPrincipals
    resourceTypes: iam.googleapis.com/AllowPolicy
    methodTypes:
      - REMOVE_GRANT
    condition:
      "resource.bindings.exists(
        binding,
        binding.members.exists(member,
          MemberSubjectMatches(member, ['user:USER_1','user:USER_2'])
        )
      )"
    actionType: DENY
    displayName: Do not allow roles to be revoked from USER_1 or USER_2  
  
Prevent principals with email addresses ending in `@gmail.com` from being granted roles.  | 
    
    
    name: organizations/ORG_ID/customConstraints/custom.dontGrantToGmail
    resourceTypes: iam.googleapis.com/AllowPolicy
    methodTypes:
      - CREATE
      - UPDATE
    condition:
      "resource.bindings.exists(
        binding,
        binding.members.exists(member,
          MemberSubjectEndsWith(member, ['@gmail.com'])
        )
      )"
    actionType: DENY
    displayName: Do not allow members whose email addresses end with "@gmail.com" to be granted roles  
  
Only allow specific roles to be granted, and only to specific principals.  | 
    
    
    name: organizations/ORG_ID/customConstraints/custom.allowSpecificRolesAndPrincipals
    resourceTypes: iam.googleapis.com/AllowPolicy
    methodTypes:
      - CREATE
      - UPDATE
    condition:
      "resource.bindings.all(
        binding,
        RoleNameMatches(binding.role, ['ROLE_1', 'ROLE_2'])  &&
        binding.members.all(member,
          MemberSubjectMatches(member, ['serviceAccount:SERVICE_ACCOUNT', 'group:GROUP'])
        )
      )"
    actionType: ALLOW
    displayName: Only allow ROLE_1 and ROLE_2 to be granted to SERVICE_ACCOUNT and GROUP  
  
Prevent Cloud Storage roles from being granted to `allUsers` and `allAuthenticatedUsers`.  | 
    
    
    name: organizations/ORG_ID/customConstraints/custom.denyStorageRolesForPrincipalAllUsers
    resourceTypes: iam.googleapis.com/AllowPolicy
    methodTypes:
      - CREATE
      - UPDATE
    condition:
      "resource.bindings.exists(
        binding,
        RoleNameStartsWith(binding.role, ['roles/storage.']) &&
        binding.members.exists(member,
          MemberSubjectMatches(member, ['allUsers', 'allAuthenticatedUsers'])
        )
      )"
    actionType: DENY
    displayName: Do not allow storage roles to be granted to allUsers or allAuthenticatedUsers  
  
Prevent any identities outside of your organization from being granted roles.  | 
    
    
    name: organizations/ORG_ID/customConstraints/custom.allowInternaldentitiesOnly
    resourceTypes: iam.googleapis.com/AllowPolicy
    methodTypes:
      - CREATE
      - UPDATE
    condition:
      "resource.bindings.all(
        binding,
        binding.members.all(member,
          MemberInPrincipalSet(member, ['//cloudresourcemanager.googleapis.com/organizations/ORG_ID'])
        )
      )"
    actionType: ALLOW
    displayName: Only allow organization members to be granted roles  
  
Only allow service accounts to be granted roles.  | 
    
    
    name: organizations/ORG_ID/customConstraints/custom.allowServiceAccountsOnly
    resourceTypes: iam.googleapis.com/AllowPolicy
    methodTypes:
      - CREATE
      - UPDATE
    condition:
      "resource.bindings.all(
        binding,
        binding.members.all(member,
          MemberTypeMatches(member, ['iam.googleapis.com/ServiceAccount'])
        )
      )"
    actionType: ALLOW
    displayName: Only allow service accounts to be granted roles  
  
Prevent removal of Google-managed service agents from role bindings.  | 
    
    
    name: organizations/ORG_ID/customConstraints/custom.denyRemovalOfGoogleManagedServiceAgents
    resource_types: iam.googleapis.com/AllowPolicy
    method_types:
      - REMOVE_GRANT
    condition: |-
      resource.bindings.all(
          binding,
          binding.members.all(member,
            MemberTypeMatches(member, ['iam.googleapis.com/ServiceAgent'])
          )
        )
    action_type: DENY
    display_name: Deny Removal Of Google-Managed Service Agents
    description: Restricts the removal of Google-managed service agents from role bindings. Please reach out to your organization admins for if you have any questions.  
  
### Conditional organization policies

You can make a custom organization policy conditional using [tags](https://docs.cloud.google.com/resource-manager/docs/organization-policy/tags-organization-policy#setting_an_organization_policy_with_tags). For example, imagine that you wrote the following custom constraint to prevent any roles that start with `roles/storage.` from being granted:
    
    
    name: organizations/ORG_ID/customConstraints/custom.dontgrantStorageRoles
    resourceTypes: iam.googleapis.com/AllowPolicy
    methodTypes:
      - CREATE
      - UPDATE
    condition:
      "resource.bindings.exists(
        binding,
        RoleNameStartsWith(binding.role, ['roles/storage.'])
      )"
    actionType: DENY
    displayName: Prevent roles that start with "roles/storage." from being granted
    

To enforce the constraint conditionally, you could create an organization policy like the following:
    
    
    name: organizations/ORG_ID/policies/custom.dontgrantStorageRoles
    spec:
      rules:
      - condition:
          expression: "resource.matchTag('ORG_ID/environment', 'dev')"
        enforce: true
      - enforce: false
    

This organization policy prevents roles that start with `roles/storage.` from being granted on any resource that also has the tag `environment=dev`.

## What's next

  * Learn more about [Organization Policy Service](https://docs.cloud.google.com/organization-policy/overview).
  * Learn more about how to [create and manage organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies).
  * See the full list of managed [organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
