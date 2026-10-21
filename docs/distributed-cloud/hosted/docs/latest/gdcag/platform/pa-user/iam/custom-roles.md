---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/custom-roles/
title: Create a custom role \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:38.477926+00:00
---

# Create a custom role  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/custom-roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a custom role Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and manage custom roles in Google Distributed Cloud (GDC) air-gapped. Custom roles let you manage access beyond the standard permission sets available in predefined roles, enabling you to configure permissions to meet your specific criteria.

Custom roles follow the principle of least privilege and are useful for granting the least access required for sensitive tasks, mitigating security risks and preventing conflicts of interest.

Creating a custom role lets you:

  * **Define the scope of access** : Choose to apply permissions across your organization, across all projects, or restrict them to specific projects.
  * **Tailor granular access** : Select one or more permissions already available through predefined roles to customize access to specific tasks or responsibilities.



Custom roles are bound by the scope in which they are created. Access to the custom role can only be granted within the same organization or project where the custom role was created.

This page is for audiences within the platform administrator group, such as IT admins or security engineers, who want to securely manage access to organizational resources. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

Visit [Predefined role descriptions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/role-descriptions) and [Role definitions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/role-definitions) for more information about roles.

## Before you begin

Before creating or managing custom roles, you must request the necessary permissions and prepare your environment.

### Request IAM organization roles

To create, update, and delete custom roles across an organization or within a project, contact your Organization IAM Admin to request the **Custom Role Org Admin** (`custom-role-org-admin`) role.

Learn more about assigning role permissions for [organizations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings).

### Request IAM project roles

To create, update, and delete custom roles within a specific project, contact your Project IAM Admin to request the **Custom Role Project Admin** (`custom-role-project-admin`) role.

Learn more about assigning role permissions for [projects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/role-bindings).

### Prepare your environment

To use the command-line tools to create or manage custom roles, complete the following setup:

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.

  * To use the API with `kubectl`, additional setup is required:

    * [Install the kubectl CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl).
    * [Generate the kubeconfig file for the global API server](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig) to configure `kubectl` access.



## View roles and their permissions

A custom role is made up of a group of permissions that you can assign to users. To create a custom role, select permissions from existing predefined roles and combine them to fit your needs. The permissions you can include in a custom role depend on the scope at which you create the role: organization or project.

This section explains how to list available roles (both predefined and custom) and view the permissions within them. You can use this information to do the following:

  * **Identify permissions for new custom roles** : Discover the specific permission strings required for the `--permissions` flag when using the gdcloud CLI to create a custom role.
  * **Review existing roles** : Examine the permissions associated with any predefined or custom role at the selected scope (organization or project).



List roles and examine their permissions using the GDC console or gdcloud CLI:

### Console

  1. Sign in to the GDC console.
  2. In the project selector, select the organization or project in which you want to view roles.
  3. In the navigation menu, click **Identity & Access > Roles**.

A list of available predefined and custom roles appears.

  4. Click a role name to view its details, including the assigned permissions.

The permissions listed for predefined roles at the current scope (organization or project) are the ones available to be included in a new custom role.




###  gdcloud 

  1. Ensure you have the gdcloud CLI installed. For more information, see the [gdcloud CLI Overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview) page.
  2. List the roles available:
         
         gdcloud iam roles list \
           --type=ROLE_TYPE \
           --project=PROJECT
         

Replace the following:

     * `ROLE_TYPE`: the type of roles to list. Valid values are `predefined`, `custom`, or `all`.
     * `PROJECT`: the project namespace where you want to view roles. Omit the `--project` flag for organization-scoped roles.
  3. View the specific permissions within a role:
         
         gdcloud iam roles describe ROLE_NAME \
           --project=PROJECT
         

Replace the following:

     * `ROLE_NAME`: the Kubernetes resource name of the role
     * `PROJECT`: the project namespace where you want to view role permissions. Omit the `--project` flag for organization-scoped roles.



See [gdcloud iam roles list](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-iam-roles-list) and [gdcloud iam roles describe](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-iam-roles-describe) for more command details and examples of usage.

## Create a custom role

Create a new custom role by grouping permissions from predefined roles together. Custom roles inherit the [IAM multi-zone capabilities](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/permissions) of the predefined roles they are built upon. After you create a custom role, you can [grant access to users](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings).

Create a custom role using the GDC console, gdcloud CLI, or the API:

### Console

  1. Sign in to the GDC console.
  2. In the project selector, select the organization or project in which you want to create a custom role.
  3. In the navigation menu, click **Identity & Access > Roles**.
  4. Click **Create Custom Role**.
  5. In the **Title** field, enter your custom role's title.
  6. In the **Description** field, provide a description of your custom role's purpose.
  7. In the **ID** field, enter the unique identifier for your custom role.

Custom role IDs can be up to 10 lowercase alphanumeric characters and can't change after role creation.

  8. Select a **Launch stage**.

  9. Select the scope of your custom role.

If you select **Organization** , the custom role applies to all resources across the organization. If you select **Projects** , the custom role applies to all current and future projects in the organization. You can select **Limit to selected projects** if you want to specify which projects can access the custom role.

  10. Click **Add Permissions**.

  11. Select the checkbox next to one or more of the supported permissions that you want to assign to your custom role.

Available permissions are limited to your selected scope. If you change scope after adding permissions, you must confirm that all previously assigned permissions reset.

  12. Click **Save.**

  13. Click **Create.**

Your new custom role appears on the **Roles** page.




###  gdcloud 

  1. Ensure you have the gdcloud CLI installed. For more information, see the [gdcloud CLI Overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview) page.
  2. Create a custom role:
         
         gdcloud iam roles create ROLE_ID \
           --title=TITLE \
           --description=DESCRIPTION \
           --permissions=PERMISSIONS
           --stage=LAUNCH_STAGE
         

Replace the following:

     * `ROLE_ID`: the unique identifier for your custom role. Custom role IDs can be up to 10 lowercase alphanumeric characters and can contain hyphens. Custom role IDs can't change after role creation.
     * `TITLE`: a user-friendly title for the custom role
     * `DESCRIPTION`: a description of the custom role's purpose
     * `PERMISSIONS`: a comma-separated list of permissions you want to grant for the custom role

For details about how to find the correct permission strings, see View roles and their permissions. Each permission string must be formatted according to the guidance in [gdcloud iam roles create](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-iam-roles-create#required_flags), where `iamRoleName` is the Kubernetes resource name of the predefined role containing the permission. You can find a role's Kubernetes resource name in the [Role definitions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/role-definitions) page or by using the [gdcloud iam roles list](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-iam-roles-list) command.

     * `LAUNCH_STAGE`: Optional. The release stage of the custom role. Valid values are `ALPHA`, `BETA`, `GA`, or `DISABLED`. Defaults to `ALPHA` if this flag is omitted.

See [gdcloud iam roles create](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-iam-roles-create) for a full list of required and optional flags, as well as examples of usage.

Alternatively, you can define the custom role in a YAML file and use the `--file` flag:
    
    gdcloud iam roles create ROLE_ID --file=YAML_FILE_PATH
    

Replace `YAML_FILE_PATH` with the path to the YAML file containing the required and optional flags. If you use the `--file` flag, all other flags such as `--title`, `--description`, and `--permissions` are ignored.




### API

**Note:** Using `kubectl` for custom role management is for advanced users.

Create and apply the `CustomRole` custom resource using `kubectl`:
    
    
    kubectl apply -f - <<EOF
    apiVersion: iam.global.gdc.goog/v1
    kind: CustomRole
    metadata:
      name: ROLE_NAME
      namespace: NAMESPACE
    spec:
      metadata:
        description: DESCRIPTION
        id: ROLE_ID
        scope: SCOPE
        stage: LAUNCH_STAGE
        title: TITLE
      RULES_TYPE:
      - RULES_LIST
    EOF
    

Replace the following:

  * `ROLE_NAME`: the Kubernetes resource name of the role
  * `NAMESPACE`: the namespace for the custom role. Use `platform` for organization-scoped roles and for multiple projects. Use the project namespace (such as `my-project`) for project-scoped roles and single projects.
  * `DESCRIPTION`: a description of the custom role's purpose
  * `ROLE_ID`: the unique identifier for your custom role. Custom role IDs can be up to 10 lowercase alphanumeric characters and can contain hyphens. Custom role IDs can't change after role creation.
  * `SCOPE`: use `organization` for roles created in the `platform` namespace. Use `project` for roles created in a project namespace.
  * `LAUNCH_STAGE`: Optional. The release stage of the custom role. Valid values are `ALPHA`, `BETA`, `GA`, or `DISABLED`. Defaults to `ALPHA` if this field is omitted.
  * `TITLE`: a user-friendly title for the custom role
  * `RULES_TYPE`: the scope of the rules. Replace with either `globalRules` (for permissions in the global API), `zonalRules` (for permissions in the zonal API), or both.
  * `RULES_LIST`: an indented list of standard Kubernetes RBAC rule objects. Each object in the list grants permissions. You can determine the correct `apiGroups`, `resources`, and `verbs` by examining the permissions within predefined roles using `gdcloud iam roles describe`, as shown in View roles and their permissions.

The following example shows the structure of a single item within a `globalRules` object:
        
        globalRules:
        - apiGroups: ["storage.global.gdc.goog"]
          resources: ["buckettypes"]
          verbs: ["get", "list", "watch"]
        

You can include multiple items in the list, each defining a different set of permissions.




## Manage a custom role

You are responsible for managing the lifecycle of your custom roles. When Distributed Cloud adds new permissions, features, or services, it updates predefined roles. Updates like deleting a predefined role or removing permissions from a predefined role can render the custom roles that rely on those permissions non-functional. You must monitor these updates and manually adjust affected custom roles to ensure they continue to work as expected.

You can edit, disable, or delete a custom role; however, you cannot edit, disable, or delete a predefined role. To view a list of all roles and their specific permissions, see View roles and their permissions.

### Edit a custom role

Edit a custom role using the GDC console, gdcloud CLI, or the API:

### Console

  1. Sign in to the GDC console.
  2. In the project selector, select the organization or project in which you want to edit a custom role.
  3. In the navigation menu, click **Identity & Access > Roles**.
  4. From the list of roles, select the custom role you want to edit.
  5. From the custom role details page, click **Edit.**
  6. Edit your custom role details such as title, description, ID, or launch stage.
  7. Optionally add or remove assigned permissions. 
     1. Click **Add permissions** to select from the list of available permissions.
     2. To remove an assigned permission, select the checkbox next to the permission you want to remove and click **Remove**.
  8. Click **Save.**

A message appears confirming your saved changes.




###  gdcloud 

  1. Ensure you have the gdcloud CLI installed. For more information, see the [gdcloud CLI Overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview) page.
  2. Edit a custom role:
         
         gdcloud iam roles update ROLE_ID \
           --title=TITLE \
           --description=DESCRIPTION \
           --permissions=PERMISSIONS
           --stage=LAUNCH_STAGE
         

Replace the following:

     * `ROLE_ID`: the unique identifier for your custom role
     * `TITLE`: a user-friendly title for the custom role
     * `DESCRIPTION`: a description of the custom role's purpose
     * `PERMISSIONS`: a comma-separated list of permissions you want to grant for the custom role

For details about how to find the correct permission strings, see View roles and their permissions. Each permission string must be formatted according to the guidance in [gdcloud iam roles create](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-iam-roles-create#required_flags), where `iamRoleName` is the Kubernetes resource name of the predefined role containing the permission. You can find a role's Kubernetes resource name in the [Role definitions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/role-definitions) page or by using the [gdcloud iam roles list](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-iam-roles-list) command.

     * `LAUNCH_STAGE`: Optional. The release stage of the custom role. Valid values are `ALPHA`, `BETA`, `GA`, or `DISABLED`. Defaults to `ALPHA` if this flag is omitted.

See [gdcloud iam roles update](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-iam-roles-update) for a full list of required and optional flags, as well as examples of usage.

Alternatively, you can update the custom role in its YAML file and use the `--file` flag:
    
    gdcloud iam roles update ROLE_ID --file=YAML_FILE_PATH
    

Replace `YAML_FILE_PATH` with the path to the YAML file containing the updated required and optional flags. If you use the `--file` flag, all other flags such as `--title`, `--description`, and `--permissions` are ignored.




### API

**Note:** Using `kubectl` for custom role management is for advanced users.

Edit a `CustomRole` custom resource using `kubectl`:
    
    
    kubectl apply -f - <<EOF
    apiVersion: iam.global.gdc.goog/v1
    kind: CustomRole
    metadata:
      name: ROLE_NAME
      namespace: NAMESPACE
    spec:
      metadata:
        description: DESCRIPTION
        id: ROLE_ID
        scope: SCOPE
        stage: LAUNCH_STAGE
        title: TITLE
      RULES_TYPE:
      - RULES_LIST
    EOF
    

Replace the following:

  * `ROLE_NAME`: the Kubernetes resource name of the role
  * `NAMESPACE`: the namespace for the custom role. Use `platform` for organization-scoped roles and for multiple projects. Use the project namespace (such as `my-project`) for project-scoped roles and single projects.
  * `DESCRIPTION`: a description of the custom role's purpose
  * `ROLE_ID`: the unique identifier for your custom role. Custom role IDs can be up to 10 lowercase alphanumeric characters and can contain hyphens. Custom role IDs can't change after role creation.
  * `SCOPE`: use `organization` for roles created in the `platform` namespace. Use `project` for roles created in a project namespace.
  * `LAUNCH_STAGE`: Optional. The release stage of the custom role. Valid values are `ALPHA`, `BETA`, `GA`, or `DISABLED`. Defaults to `ALPHA` if this field is omitted.
  * `TITLE`: a user-friendly title for the custom role
  * `RULES_TYPE`: the scope of the rules. Replace with either `globalRules` (for permissions in the global API), `zonalRules` (for permissions in the zonal API), or both.
  * `RULES_LIST`: an indented list of standard Kubernetes RBAC rule objects. Each object in the list grants permissions. You can determine the correct `apiGroups`, `resources`, and `verbs` by examining the permissions within predefined roles using `gdcloud iam roles describe`, as shown in View roles and their permissions.

The following example shows the structure of a single item within a `globalRules` object:
        
        globalRules:
        - apiGroups: ["storage.global.gdc.goog"]
          resources: ["buckettypes"]
          verbs: ["get", "list", "watch"]
        

You can include multiple items in the list, each defining a different set of permissions.




### Disable a custom role

Disabled custom roles remain in your list of roles and can still be assigned to users; however, the role has no effect. You can re-enable the custom role at any time.

Disable a custom role using the GDC console, gdcloud CLI, or the API:

### Console

  1. Sign in to the GDC console.
  2. In the project selector, select the organization or project in which you want to disable a custom role.
  3. In the navigation menu, click **Identity & Access > Roles**.
  4. In the list of roles, select the custom role you want to disable.
  5. On the custom role details page, click **Disable.**



###  gdcloud 

  1. Ensure you have the gdcloud CLI installed. For more information, see the [gdcloud CLI Overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview) page.
  2. Disable a custom role:
         
         gdcloud iam roles update ROLE_ID --stage=DISABLED
         

Replace the following:

     * `ROLE_ID`: the unique identifier for your custom role

See [gdcloud iam roles update](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-iam-roles-update) for more information.




### API

**Note:** Using `kubectl` for custom role management is for advanced users.

Disable a `CustomRole` custom resource by changing the `stage` field to `DISABLED`. Make sure all other fields match the current values for the custom role you want to disable.
    
    
    kubectl apply -f - <<EOF
    apiVersion: iam.global.gdc.goog/v1
    kind: CustomRole
    metadata:
      name: ROLE_NAME
      namespace: NAMESPACE
    spec:
      metadata:
        description: DESCRIPTION
        id: ROLE_ID
        scope: SCOPE
        stage: DISABLED
        title: TITLE
      RULES_TYPE:
      - RULES_LIST
    EOF
    

Replace the following:

  * `ROLE_NAME`: the Kubernetes resource name of the role
  * `NAMESPACE`: the namespace for the custom role. Use `platform` for organization-scoped roles and for multiple projects. Use the project namespace (such as `my-project`) for project-scoped roles and single projects.
  * `DESCRIPTION`: a description of the custom role's purpose
  * `ROLE_ID`: the unique identifier for your custom role. Custom role IDs can be up to 10 lowercase alphanumeric characters and can contain hyphens. Custom role IDs can't change after role creation.
  * `SCOPE`: use `organization` for roles created in the `platform` namespace. Use `project` for roles created in a project namespace.
  * `TITLE`: a user-friendly title for the custom role
  * `RULES_TYPE`: the scope of the rules. Replace with either `globalRules` (for permissions in the global API), `zonalRules` (for permissions in the zonal API), or both.
  * `RULES_LIST`: an indented list of standard Kubernetes RBAC rule objects. Each object in the list grants permissions. You can determine the correct `apiGroups`, `resources`, and `verbs` by examining the permissions within predefined roles using `gdcloud iam roles describe`, as shown in View roles and their permissions.

The following example shows the structure of a single item within a `globalRules` object:
        
        globalRules:
        - apiGroups: ["storage.global.gdc.goog"]
          resources: ["buckettypes"]
          verbs: ["get", "list", "watch"]
        

You can include multiple items in the list, each defining a different set of permissions.




### Delete a custom role

Deleted roles are permanently removed from the system; however, you can create a new role with the same name.

Delete a custom role using the gdcloud CLI or the API:

###  gdcloud 

  1. Ensure you have the gdcloud CLI installed. For more information, see the [gdcloud CLI Overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview) page.
  2. Delete a custom role:
         
         gdcloud iam roles delete ROLE_ID --project=PROJECT
         

Replace the following:

     * `ROLE_ID`: the unique identifier for your custom role
     * `PROJECT`: the project namespace where you want to delete the custom role. If the `--project` flag isn't specified, the organization-scoped role is deleted.

See [gdcloud iam roles delete](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-iam-roles-delete) for more information and examples of usage.




### API

**Note:** Using `kubectl` for custom role management is for advanced users.

Delete a `CustomRole` custom resource using `kubectl`:
    
    
    kubectl delete -f CUSTOM_ROLE
    

Replace `CUSTOM_ROLE` with the path to your `CustomRole` YAML file. This is the same file that you used to create or update the role.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
