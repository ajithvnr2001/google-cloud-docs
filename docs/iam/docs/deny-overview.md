---
url: https://docs.cloud.google.com/iam/docs/deny-overview/
title: Deny policies \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:10.042140+00:00
---

# Deny policies  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/deny-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Deny policies Stay organized with collections  Save and categorize content based on your preferences. 

Identity and Access Management (IAM) deny policies let you set guardrails on access to Google Cloud resources. With deny policies, you can define _deny rules_ that prevent certain principals from using certain permissions, regardless of the roles they're granted.

This page provides an overview of deny policies and deny rules. To learn how to create and update deny policies, see [Deny access to resources](https://docs.cloud.google.com/iam/docs/deny-access).

## How deny policies work

Deny policies are made up of deny rules. Each deny rule specifies the following:

  * A set of principals that are denied permissions
  * The permissions that the principals are _denied_ , or unable to use
  * Optional: The condition that must be true for the permission to be denied



When a principal is denied a permission, they can't do anything that requires that permission, regardless of the IAM roles they've been granted. This is because IAM always checks relevant deny policies before checking relevant allow policies. For details, see [policy evaluation](https://docs.cloud.google.com/iam/docs/policy-types#evaluation).

To specify where you want a deny policy to apply, you attach it to a project, folder, or organization. When a deny policy is attached to one of these resources, the principals in the policy can't use the specified permissions to access the resource, or any of the resource's descendants. To learn more about where you can attach a deny policy, see Attachment point on this page.

You can attach multiple deny policies to a single resource. This lets you create separate deny policies for different types of deny rules. For example, you could put compliance-related deny rules in one policy, then use another policy for other deny rules. Each deny policy is evaluated independently of all other deny policies.

Each resource can have up to 500 deny policies. Together, these deny policies can contain a total of 500 deny rules.

**Note:** Changes to a principal's access are [eventually consistent](https://wikipedia.org/wiki/Eventual_consistency). This means that it takes time for access changes to propagate through the system. To learn how long it takes, on average, for access changes to propagate, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation). 

### Attachment point

Each deny policy is attached to an organization, folder, or project. When attached to one of these resources, deny policies are inherited by all lower-level resources in that project, folder, or organization. To work with deny policies, you need an identifier for the resource that the deny policy is attached to, which is called the _attachment point_. This identifier uses one of the formats in the following table:

Attachment point format  
---  
Organization |  `cloudresourcemanager.googleapis.com/organizations/ORG_ID`  
Replace `ORG_ID` with the numeric organization ID. For the REST API, URL-encode the entire value.  Example for the gcloud CLI:  
`cloudresourcemanager.googleapis.com/organizations/123456789012` Example for the REST API:  
`cloudresourcemanager.googleapis.com%2Forganizations%2F123456789012`  
Folder |  `cloudresourcemanager.googleapis.com/folders/FOLDER_ID`  
Replace `FOLDER_ID` with the numeric folder ID. For the REST API, URL-encode the entire value.  Example for the gcloud CLI:  
`cloudresourcemanager.googleapis.com/folders/987654321098` Example for the REST API:  
`cloudresourcemanager.googleapis.com%2Ffolders%2F987654321098`  
Project |  `cloudresourcemanager.googleapis.com/projects/PROJECT_ID`  
Replace `PROJECT_ID` with the alphanumeric or numeric project ID. For the REST API, URL-encode the entire value.  Example for the gcloud CLI:  
`cloudresourcemanager.googleapis.com/projects/my-project` Example for the REST API:  
`cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-project`  
  
### Deny policy inheritance

Deny policies, like allow policies, are inherited through the [resource hierarchy](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control). When you attach a deny policy to a project, folder, or organization, the policy is also effective for all resources inside that project, folder, or organization.

For example, if a deny policy for an _organization_ says that a principal cannot use a specific permission, then the principal cannot use that permission for _any_ resource within the organization. This rule applies even if the folders and projects within that organization have more permissive deny policies.

Similarly, if a deny policy for a _project_ says that a principal cannot use a specific permission, then the principal cannot use that permission for _any_ resource within the project. This rule applies even if the parent organization and folders have more permissive deny policies.

### Denial conditions

Denial conditions specify the conditions that must be met in order for a deny rule to apply. If the condition evaluates to `true` or cannot be evaluated, the deny rule applies and the principals are unable to use the specified permissions. If the condition evaluates to `false`, the deny rule does not apply and the principals can use the specified permissions if they have them.

Denial conditions have the same structure as IAM Conditions. However, denial conditions only recognize [resource tag functions](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resource-tags).

To learn how to write conditions, see [overview of IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview).

### Permission groups

Some services let you deny _permission groups_. Permission groups are sets of permissions that match a specified pattern. You can use a permission group to deny sets of related permissions—for example, you can deny all permissions for a single service or resource.

Supported permission groups are listed in [Permissions supported in deny policies](https://docs.cloud.google.com/iam/docs/deny-permissions-support). The identifiers for the supported permission groups replace one or more sections of a permission name with a wildcard character (`*`). The permissions that each group includes depend on the position of the wildcard:

  * `SERVICE_FQDN/RESOURCE.*`: Denies all permissions for the specified given resource.
  * `SERVICE_FQDN/*.*`: Denies all permissions for the specified service.
  * `SERVICE_FQDN/*.VERB`: Denies all permissions for a service that end in the specified verb.



Permission groups include all current and future permissions that match the specified pattern. For example, imagine that you use the permission group `example.googleapis.com/exampleResource.*` to deny a user all permissions for the `exampleResource` resource type. If `example.googleapis.com` adds a new permission for the `exampleResource` resource type, such as `example.googleapis.com/exampleResource.newPermission`, the user will automatically be denied the new permission.

You can only use wildcards in supported permission groups. Using wildcards in other permission names is not supported.

## Structure of a deny policy

A deny policy is a collection of metadata and _deny rules_. A deny rule associates a set of principals with a set of permissions that the principals are denied, or unable to use. Each rule can also specify a condition that determines when the permission is denied.

For example, the following deny policy blocks all principals from deleting projects, unless the principal is a member of the `project-admins` group or the project being deleted has a tag with the value `test`.
    
    
    {
      "name": "policies/cloudresourcemanager.googleapis.com%2Fprojects%2F253519172624/denypolicies/limit-project-deletion",
      "uid": "06ccd2eb-d2a5-5dd1-a746-eaf4c6g3f816",
      "kind": "DenyPolicy",
      "displayName": "Only project admins can delete projects.",
      "etag": "MTc1MTkzMjY0MjUyMTExODMxMDQ=",
      "createTime": "2021-09-07T23:15:35.258319Z",
      "updateTime": "2021-09-07T23:15:35.258319Z",
      "rules": [
        {
          "denyRule": {
            "deniedPrincipals": [
              "principalSet://goog/public:all"
            ],
            "exceptionPrincipals": [
              "principalSet://goog/group/project-admins@example.com"
            ],
            "deniedPermissions": [
              "cloudresourcemanager.googleapis.com/projects.delete",
              "cloudresourcemanager.googleapis.com/folders.*"
            ],
            "exceptionPermissions": [
              "cloudresourcemanager.googleapis.com/folders.list",
              "cloudresourcemanager.googelapis.com/folders.get"
            ],
            "denialCondition": {
              "title":  "Only for non-test projects",
              "expression": "!resource.matchTag('12345678/env', 'test')"
            }
          }
        }
      ]
    }
    

The following sections describe the fields in a deny policy's metadata and deny rules.

### Metadata

Deny policies contain the following metadata:

  * `name`: The name of the deny policy. This name has the format `policies/ATTACHMENT_POINT/denypolicies/POLICY_ID`, where `ATTACHMENT_POINT` is the project, folder, or organization that the deny policy is attached to and `POLICY_ID` is the deny policy's alphanumeric ID.
  * `uid`: A unique ID assigned to the deny policy by Google.
  * `kind`: The type of policy. The `kind` for a deny policy is always `DenyPolicy`.
  * `displayName`: Optional. A human-readable name for the deny policy.
  * `etag`: An identifier for a version of the policy. To prevent conflicting updates, the `etag` value must match the value that is stored in IAM. If the `etag` values do not match, the request fails.
  * `createTime`: The time when the deny policy was created.
  * `updateTime`: The last time that the deny policy was updated.



### Deny rules

Each deny rule can have the following fields:

  * `deniedPrincipals`: The principals that are denied permissions. You can list individual principals and sets of principals. Individual principal types include user accounts, service accounts, and single identities in a workforce or workload identity pool. Sets of principals include Google groups, Cloud Identity domains, sets of workforce or workload identities, and all users on the internet.

For a list of valid principal types and identifiers, see [Principal identifiers for deny policies](https://docs.cloud.google.com/iam/docs/principal-identifiers#deny).

  * `exceptionPrincipals`: Optional. The principals that are exempt from the deny rule. These principals are not denied the specified permissions even if they are listed in `deniedPrincipals`, or are part of a group listed in `deniedPrincipals`.

You can list individual principals and sets of principals. Individual principal types include user accounts, service accounts, and single identities in a workforce or workload identity pool. Sets of principals include Google groups, Cloud Identity domains, sets of workforce or workload identities, and all users on the internet.

For a list of valid principal types and identifiers, see [Principal identifiers for deny policies](https://docs.cloud.google.com/iam/docs/principal-identifiers#deny).

  * `deniedPermissions`: The permissions that the specified principals are unable to use, or denied. These permissions use the IAM `v2` permission format, which uses fully qualified domain names (FQDNs) to identify the service. The format is `SERVICE_FQDN/RESOURCE.ACTION`. Google APIs use the domain `*.googleapis.com`. For example, `iam.googleapis.com/roles.delete`.

Only some permissions can be denied. For a full list of permissions that can be denied, see [Permissions supported in deny policies](https://docs.cloud.google.com/iam/docs/deny-permissions-support).

In some cases, you can also use permission groups to deny sets of permissions. For more information, see Permission groups.

  * `exceptionPermissions`: Optional. A list of permissions that the specified principals can use, even if those permissions are included in `deniedPermissions`. For example, you can use this field to make exceptions for specific permissions in a permission group.

  * `denialConditions`: Optional. A logic expression that affects when the deny rule applies. If the condition evaluates to `true` or cannot be evaluated, the permission is denied. If the condition evaluates to `false`, the permission is not denied. For more information, see Denial conditions on this page.




## Common use cases

The following are common situations where you might want to use deny policies, and examples of the deny rules you might create in each situation. To learn how to create and update deny policies, see [Deny access to resources](https://docs.cloud.google.com/iam/docs/deny-access).

### Centralizing administrative privileges

You can use deny policies to restrict certain types of administrative activities to a specific set of principals.

For example, imagine you want to limit custom role management for your organization to a single central team. To do so, you create a deny rule that denies the permissions required for custom role management to all users, except users in the administrative group (`custom-role-admins`):
    
    
    {
      "deniedPrincipals": [
        "principalSet://goog/public:all"
      ],
      "exceptionPrincipals": [
        "principalSet://goog/group/custom-role-admins@example.com"
      ],
      "deniedPermissions": [
        "iam.googleapis.com/roles.create",
        "iam.googleapis.com/roles.delete",
        "iam.googleapis.com/roles.update",
      ]
    }
    

Then, you attach the deny policy to your organization.

![](https://docs.cloud.google.com/static/iam/img/deny-centralize-admin-privileges-1.svg)

![](https://docs.cloud.google.com/static/iam/img/deny-centralize-admin-privileges-1.svg)

Now, only members of the `custom-role-admins` group are able to manage custom roles, even if other users have the required permissions.

For example, imagine that both Yuri and Tal have the Organization Role Administrator role (`roles/iam.organizationRoleAdmin`). However, Yuri is a member of `custom-role-admins`, and Tal is not. With this deny policy, only Yuri is able to create, delete, and update roles.

![](https://docs.cloud.google.com/static/iam/img/deny-centralize-admin-privileges-2.svg)

![](https://docs.cloud.google.com/static/iam/img/deny-centralize-admin-privileges-2.svg)

### Creating exceptions to access grants

You can use deny policies to deny inherited permissions. This capability gives you the option to grant a role at a high level in the resource hierarchy, and then deny the role's permissions on individual lower-level resources if necessary.

For example, imagine that you have a folder, `Engineering`, that contains multiple projects. You want to give a group, `eng`, the permissions in the Service Account Key Admin role (`roles/iam.serviceAccountKeyAdmin`) on almost all of the projects in the folder. However, you _don't_ want the group to gain the ability to create and delete service account keys in one specific project in the folder, `example-prod`.

Instead of granting the Service Account Key Admin role on each individual project, you create the following deny rule, which denies create and delete permissions in the Service Account Key Admin role to the principals in the `eng` group:
    
    
    {
      "deniedPrincipals": [
        "principalSet://goog/group/eng@example.com"
      ],
      "deniedPermissions": [
        "iam.googleapis.com/serviceAccountKeys.create",
        "iam.googleapis.com/serviceAccountKeys.delete"
      ]
    }
    

Then, you add this deny rule to a deny policy and attach the policy to the project `example-prod`.

After you attach the deny policy to the project, you can grant the Service Account Key Admin role to the `eng` group on the `Engineering` folder without letting the group create or delete service account keys in `example-prod`.

![](https://docs.cloud.google.com/static/iam/img/deny-exceptions-to-access-grants-1.svg)

![](https://docs.cloud.google.com/static/iam/img/deny-exceptions-to-access-grants-1.svg)

Members of the `eng` group are then able to create and delete service account keys in all projects except `example-prod`. For example, if Izumi is a member of the `eng` group, they can create and delete keys for service accounts in `example-dev` and `example-test`, but not in `example-prod`.

![](https://docs.cloud.google.com/static/iam/img/deny-exceptions-to-access-grants-2.svg)

![](https://docs.cloud.google.com/static/iam/img/deny-exceptions-to-access-grants-2.svg)

However, imagine that you actually want a subset of the `eng` group to be able to create and delete service account keys in `example-prod`. This subset is represented by the group `eng-prod`. To allow the members of the `eng-prod` group to create and delete service account keys in `example-prod`, you can make the group exempt from the deny rule:
    
    
    {
      "deniedPrincipals": [
        "principalSet://goog/group/eng@example.com"
      ],
      **"exceptionPrincipals" : [
        "principalSet://goog/group/eng-prod@example.com"
      ],**
      "deniedPermissions": [
        "iam.googleapis.com/serviceAccountKeys.create",
        "iam.googleapis.com/serviceAccountKeys.delete"
      ]
    }
    

With this revised deny policy, members of the `eng-prod` group can create and delete service account keys in all projects, including `example-prod`. For example, if Charlie is a member of the `eng-prod` group, they can create and delete keys in `example-dev`, `example-test`, and `example-prod`, even if they are also a member of the `eng` group.

![](https://docs.cloud.google.com/static/iam/img/deny-exceptions-to-access-grants-3.svg)

![](https://docs.cloud.google.com/static/iam/img/deny-exceptions-to-access-grants-3.svg)

### Blocking access based on tags

A tag is a key-value pair that can be attached to an organization, folder, or project. You can use deny policies to deny permissions based on tags without adding an IAM Condition to every role grant.

For example, imagine that you tag all of your projects as `dev`, `test`, or `prod`. You want only members of the `project-admins` group to be able to delete projects that are tagged `prod`.

To solve this problem, you create a deny rule that denies the `cloudresourcemanager.googleapis.com/projects.delete` permission to everyone except the `project-admins` group for resources that are tagged `prod`:
    
    
    {
      "displayName": "Only project admins can delete production projects.",
      "rules": [
        {
          "denyRule": {
            "deniedPrincipals": [
              "principalSet://goog/public:all"
            ],
            "exceptionPrincipals": [
              "principalSet://goog/group/project-admins@example.com"
            ],
            "deniedPermissions": [
              "cloudresourcemanager.googleapis.com/projects.delete"
            ],
            "denialCondition": {
              "title":  "Only for prod projects",
              "expression": "resource.matchTag('12345678/env', 'prod')"
            }
          }
        }
      ]
    }
    

Then, you add this deny rule to a deny policy and attach the policy to your organization.

![](https://docs.cloud.google.com/static/iam/img/deny-block-access-based-on-tags-1.svg)

![](https://docs.cloud.google.com/static/iam/img/deny-block-access-based-on-tags-1.svg)

Because of this deny rule, you can limit principals' access without adding a condition to their role grants. Instead, you can grant principals roles that contain the `cloudresourcemanager.googleapis.com/projects.delete` permission, and rely on the deny rule to prevent principals outside of the `project-admins` group from deleting any projects tagged `prod`.

For example, consider two users, Bola and Kiran. Both users have the Project Deleter role (`roles/resourcemanager.projectDeleter`). Additionally, Kiran is a member of the `project-admins` group. With this deny policy, Bola can only delete projects that have the tag `dev` or `test`. Kiran can delete all projects, regardless of their tags.

![](https://docs.cloud.google.com/static/iam/img/deny-block-access-based-on-tags-2.svg)

![](https://docs.cloud.google.com/static/iam/img/deny-block-access-based-on-tags-2.svg)

## What's next

  * Learn how to [create, update, and delete deny policies](https://docs.cloud.google.com/iam/docs/deny-access).
  * Find out how to [troubleshoot access issues with deny policies](https://docs.cloud.google.com/iam/docs/troubleshoot-policies).
  * Review the [permissions that can be denied](https://docs.cloud.google.com/iam/docs/deny-permissions-support).
  * See the [types of principals](https://docs.cloud.google.com/iam/docs/principal-identifiers#deny) that you can include in deny policies.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
