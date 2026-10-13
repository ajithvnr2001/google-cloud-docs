---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/set-up-role-bindings/
title: Grant and revoke access \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:40.258598+00:00
---

# Grant and revoke access  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/set-up-role-bindings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Grant and revoke access Stay organized with collections  Save and categorize content based on your preferences. 

Every subject - a user or a group - follows a two-step process to gain access to the Management API server and Kubernetes cluster:

  * **Management API server access:** Grant a subject with permissions in the Management API server using `ClusterRoleBinding` or `RoleBinding` to a predefined `ClusterRole`.

  * **Kubernetes cluster access:** Grant namespace-specific access or cluster-wide access.

    * **For namespace-specific access:** To grant access to a specific project's namespace within the cluster, create a `ProjectRole` and corresponding `ProjectRoleBinding`. This process propagates a Kubernetes `Role` and `RoleBinding` to a Kubernetes `Namespace` in the cluster, which corresponds to the `Project` that the `ProjectRole` and `ProjectRoleBinding` are associated with.

    * **For cluster-wide access:** To grant access to all namespaces within the cluster, create an `OrganizationRole` and corresponding `OrganizationRoleBinding`. This process propagates a Kubernetes `ClusterRole` and `ClusterRoleBinding` to the entire Kubernetes cluster.


**Note:** You can bind one subject to multiple roles in the Management API server and Kubernetes clusters. Permissions are purely additive, and there are no deny rules.**Note:** You can grant a subject with only Kubernetes cluster access through a `ProjectRole` and `ProjectRoleBinding` that another person has created. The subject has no access in the Management API server.

This page is for audiences within the platform administrator group who manage permissions within their organization.

Both the Organization IAM Admin and the Project IAM Admin can create more project roles and project role bindings to grant additional project-specific permissions. However, Organization IAM Admins can create project roles and project role bindings for any project. On the other hand, Project IAM Admins can only create project roles and project role bindings for projects they have permission to access.

## Before you begin

Before managing role bindings or revoking access, you must request the necessary permissions and prepare your environment. The specific roles required depend on whether you are managing role bindings or revoking user access.

### Request IAM roles

Contact your Organization IAM Admin to request the roles based on the tasks you need to perform:

  * **Organization IAM Admin** (`organization-iam-admin`): create, update, and delete role bindings at the organization and project levels.
  * **Org Session Admin** (`org-session-admin`): revoke a user's active sessions and access within a specific zone.



### Prepare your environment

To use the command-line tools for managing role bindings or revoking access, complete the following setup.

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.
  * To use the API with `kubectl`, additional setup is required: 
    * [Install the kubectl CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/get-started/kubectl).
    * [Generate the kubeconfig file for the global API server](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in#global-resources-kubeconfig).



## Set up role bindings

You can set up role bindings that give team members access to resources at the organization or project level.

To get the permissions that you need to set up role bindings, ask your Organization IAM Admin to grant you the Organization IAM Admin role.

To assign a role to an authorized member, follow these steps:

###  Console 

  1. Sign in to the GDC console.
  2. Click **Select project** to select an organization or project.  
![](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/images/select-project-ui.png)
     * To set up role bindings for an organization, select an organization.
     * To set up role bindings for a project, select a project.
  3. In the navigation menu, click **Identity and Access > Access**.
  4. Click **Add member**.
  5. In the **Identity provider** list, select an identity provider.
  6. Choose whether you want to add individual users or groups.
  7. In the **Username or group alias** field, enter the username, email address, or alias.
  8. In the **Role** list, select the role that you want to assign to the user or group, such as **Organization Viewer** at the organization level or **Project Creator** at the project level.
  9. Click **Add**.



The member appears in the **Authorized member** list.

###  gdcloud 

  1. Ensure you have the [gdcloud CLI installed](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview#download-and-install).

  2. Sign in using the `gdcloud auth login` command to authenticate with your identity provider. For more information, see [the gdcloud CLI authentication](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-auth#login).

  3. Set up role bindings.

     * Set up role bindings for an organization:
           
           gdcloud organizations add-iam-policy-binding root \
             --member=USER_ACCOUNT \
             --role=ROLE_TYPE/ROLE
           

Replace the following variables:

       * `USER_ACCOUNT`: the user account to which you want to grant the role. This flag accepts either a user email address with the identity provider prefix (`user:idpprefix-user@example.com`) or a service account name with the service account project (`serviceAccount:projectName:serviceAccountName`).
       * `ROLE_TYPE`: the `ClusterRole`, `Role`, or `OrganizationRole` for which you're setting up the role binding.
       * `ROLE`: the name of the predefined or custom role you want to assign to the user (such as `project-creator`).
     * Set up role bindings for a project:
           
           gdcloud projects add-iam-policy-binding PROJECT \
             --member=USER_ACCOUNT \
             --role=ROLE_TYPE/ROLE
           

Replace the following variables:

       * `PROJECT`: the name of the project for which you're setting up the role binding.
       * `USER_ACCOUNT`: the user account to which you want to grant the role. This flag accepts either a user email address with the identity provider prefix (`user:idpprefix-user@example.com`) or a service account name with the service account project (`serviceAccount:projectName:serviceAccountName`).
       * `ROLE_TYPE`: the `Role` or `ProjectRole` for which you're setting up the role binding.
       * `ROLE`: the name of the predefined or custom role you want to assign to the user (such as `project-viewer`).



###  API 

**Note:** The API instructions are for advanced users.

  1. Export the environment variables for the role binding:
         
         export YOUR_IAM_ADMIN_KUBECONFIG=YOUR_IAM_ADMIN_KUBECONFIG
         export USERNAME=IDP_PREFIX-USERNAME
         export ROLE_NAME=ROLE_NAME
         export USER_EMAIL=IDP_PREFIX-USER_EMAIL
         

Replace the following:

     * `YOUR_IAM_ADMIN_KUBECONFIG`: the path to the kubeconfig file for the IAM administrator.
     * `IDP_PREFIX`: the identity provider prefix.
     * `USERNAME`: the username portion of the user's email address before the `@` symbol (such as `paul` from `paul@example.com`).
     * `ROLE_NAME`: the name of the role the user needs (such as `project-creator`). See [Role definitions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/role-definitions) for details about the role.
     * `USER_EMAIL`: the email address of the user account for which you want to assign the role (such as `paul@example.com`).
  2. Assign a user to a `ClusterRole`, `Role`, `ProjectRole`, or `OrganizationRole`:

     * Assign a user to a `ClusterRole`:
           
           kubectl create --kubeconfig ${YOUR_IAM_ADMIN_KUBECONFIG} \
           clusterrolebinding ${USERNAME}-${ROLE_NAME}-binding \
           --clusterrole=${ROLE_NAME} --user=${USER_EMAIL}
           

For cases when a `ClusterRole` requires a `RoleBinding` instead of a `ClusterRoleBinding`, refer to the [Role definitions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/role-definitions) to find out what binding type the role needs and create a RoleBinding in the namespace `gpc-system` instead:
           
           kubectl create --kubeconfig ${YOUR_IAM_ADMIN_KUBECONFIG} \
           rolebinding ${USERNAME}-${ROLE_NAME}-binding \
           --clusterrole=${ROLE_NAME} --user=${USER_EMAIL} --namespace=gpc-system
           

     * Assign a user to a `Role`:

       1. Export the namespace where the binding must be created:
              
              export BINDING_NAMESPACE=BINDING_NAMESPACE
              

       2. Run the following commands to create a `RoleBinding`:
              
              kubectl create --kubeconfig ${YOUR_IAM_ADMIN_KUBECONFIG} \
              rolebinding ${USERNAME}-${ROLE_NAME}-binding \
              --role=${ROLE_NAME} --user=${USER_EMAIL} --namespace=${BINDING_NAMESPACE}
              

     * Assign a user to a `ProjectRole`:

       1. Create a `projectrolebinding.yaml` file:
              
              apiVersion: resourcemanager.gdc.goog/v1
              kind: ProjectRoleBinding
              metadata:
                name: BINDING_NAME
                namespace: PROJECT_NAME
              spec:
                roleRef:
                  apiGroup: resourcemanager.gdc.goog
                  kind: ProjectRole
                  name: ROLE_NAME
                subjects:
                - apiGroup: rbac.authorization.k8s.io
                  kind: USER_KIND
                  name: IDP_PREFIX-USER_EMAIL
              

Replace the following:

          * `BINDING_NAME`: a name for the binding that the user can customize (such as `user-project-creator-binding`).
          * `PROJECT_NAME`: the name of the project to which you're granting the role.
          * `ROLE_NAME`: the name of the `ProjectRole` you're assigning to the user.
          * `USER_KIND`: the kind of user, which can be `User`, `Group`, or `ServiceAccount`.
          * `IDP_PREFIX`: the identity provider prefix.
          * `USER_EMAIL`: the email address of the user account for which you want to assign the role (such as `paul@example.com`).
       2. Apply the `projectrolebinding.yaml` file:
              
              kubectl create -f projectrolebinding.yaml
              

     * Assign a user to an `OrganizationRole`:

       1. Create an `organizationrolebinding.yaml` file:
              
              apiVersion: resourcemanager.gdc.goog/v1
              kind: OrganizationRoleBinding
              metadata:
                name: BINDING_NAME
                namespace: gpc-system
              spec:
                roleRef:
                  apiGroup: resourcemanager.gdc.goog
                  kind: OrganizationRole
                  name: ROLE_NAME
                subjects:
                - apiGroup: rbac.authorization.k8s.io
                  kind: USER_KIND
                  name: IDP_PREFIX-USER_EMAIL
              

Replace the following:

          * `BINDING_NAME`: a name for the binding that the user can customize (such as `user-organization-creator-binding`).
          * `ROLE_NAME`: the name of the `OrganizationRole` you're assigning to the user.
          * `USER_KIND`: the kind of user, which can be `User`, `Group`, or `ServiceAccount`.
          * `IDP_PREFIX`: the identity provider prefix.
          * `USER_EMAIL`: the email address of the user account for which you want to assign the role (such as `paul@example.com`).
       2. Apply the `organizationrolebinding.yaml` YAML file:
              
              kubectl create -f organizationrolebinding.yaml
              




## Remove role bindings

When access is no longer required, remove a member and their associated roles, permissions, and access.

To remove members, work through the following steps:

###  Console 

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Identity and Access > Access**.
  3. In the **Authorized members** list, select a member.
  4. Click **Remove member**.
  5. When prompted, click **Remove member** to confirm.



###  gdcloud 

  1. Ensure you have the [gdcloud CLI installed](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview#download-and-install).

  2. Sign in using the `gdcloud auth login` command to authenticate with your identity provider. For more information, see [the gdcloud CLI authentication](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-auth#login).

  3. Remove role bindings.

     * Remove role bindings for an organization:
           
           gdcloud organizations remove-iam-policy-binding root \
             --member=USER_ACCOUNT \
             --role=ROLE_TYPE/ROLE
           

Replace the following variables:

       * `USER_ACCOUNT`: the user account from which you want to remove the role. This flag accepts either a user email address with the identity provider prefix (`user:idpprefix-user@example.com`) or a service account name with the service account project (`serviceAccount:projectName:serviceAccountName`).
       * `ROLE_TYPE`: the `ClusterRole`, `Role`, or `OrganizationRole` for which you're removing the role binding.
       * `ROLE`: the name of the predefined or custom role you want to remove from the user account (such as `project-creator`).
     * Remove role bindings for a project:
           
           gdcloud projects remove-iam-policy-binding PROJECT \
             --member=USER_ACCOUNT \
             --role=ROLE_TYPE/ROLE
           

Replace the following variables:

       * `PROJECT`: the name of the project from which you're removing the role binding.
       * `USER_ACCOUNT`: the user account from which you want to remove the role. This flag accepts either a user email address with the identity provider prefix (`user:idpprefix-user@example.com`) or a service account name with the service account project (`serviceAccount:projectName:serviceAccountName`).
       * `ROLE_TYPE`: the `Role` or `ProjectRole` for which you're removing the role binding.
       * `ROLE`: the name of the predefined or custom role you want to remove from the user account (such as `project-viewer`).



###  API 

**Note:** The API instructions are for advanced users.

  1. Export the environment variables for the role binding:
         
         export YOUR_IAM_ADMIN_KUBECONFIG=YOUR_IAM_ADMIN_KUBECONFIG
         export USERNAME=IDP_PREFIX-USERNAME
         export BINDING_NAMESPACE=BINDING_NAMESPACE
         

Replace the following:

     * `YOUR_IAM_ADMIN_KUBECONFIG`: the path to the kubeconfig file for the IAM administrator.
     * `IDP_PREFIX`: the identity provider prefix.
     * `USERNAME`: the username portion of the user's email address before the `@` symbol (such as `paul` from `paul@example.com`).
     * `BINDING_NAMESPACE`: the namespace where the binding is being removed.
  2. Delete the `ClusterRoleBinding`, `RoleBinding`, `ProjectRoleBinding`, or `OrganizationRoleBinding` to revoke the permission granted to the user account:

     * Remove the `ClusterRoleBinding` from a user account:
           
           kubectl --kubeconfig ${YOUR_IAM_ADMIN_KUBECONFIG} \
           delete clusterrolebinding ${USERNAME}-pa
           

     * Remove the `RoleBinding` from a user account:
           
           kubectl --kubeconfig ${YOUR_IAM_ADMIN_KUBECONFIG} \
           delete rolebinding ${USERNAME}-pa \
           --namespace=${BINDING_NAMESPACE}
           

     * Remove the `ProjectRoleBinding` from a user account:
           
           kubectl --kubeconfig ${YOUR_IAM_ADMIN_KUBECONFIG} \
           delete projectrolebinding ${USERNAME}-pa \
           --namespace=${BINDING_NAMESPACE}
           

     * Remove the `OrganizationRoleBinding` from a user account:
           
           kubectl --kubeconfig ${YOUR_IAM_ADMIN_KUBECONFIG} \
           delete organizationrolebinding ${USERNAME}-pa \
           --namespace=gpc-system
           




## Revoke user access

If a member leaves your organization or team, you can revoke their access to Google Distributed Cloud (GDC) air-gapped appliance. Revoking a user's access logs them out of GDC air-gapped appliance and removes their roles and permissions. You can also list the user's activity and sessions from their start and end time.

To revoke a user's access, do the following:

  1. Get the permissions that you need to revoke users. Ask your Organization IAM Admin to grant you the Org Session Admin (`org-session-admin`) role.

  2. Revoke the user's access:
         
         gdcloud admin auth revoke --accounts USER_EMAIL
         

Replace USER_EMAIL with the email of the user to revoke access.

After running the command, you see output similar to the following. This example revokes access from the user `ariel@example.com`:
         
         Success: NUMBER of sessions revoked for user ariel@example.com
         

In this example, the variable NUMBER refers to the number of active sessions the user had.

  3. Confirm you've revoked the user's access by running the `gdcloud admin auth revoke` command again. If successful, you see the following:
         
         No sessions found for account: ariel@example.com
         




### List all revoked users

To view all revoked users and their activity and sessions, do the following:

  * List all revoked users from their start and end time:
        
        gdcloud admin auth list --format="csv(ACCOUNT, IDENTITY_PROVIDER, CREATION_TIME, EXPIRATION_TIME)"
        

If successful, you see output similar to the following:
        
        account,identity_provider,creation_time,expiration_time
        ariel@example.com,example-idp,2023-02-15 22:10:52,2023-02-15 23:10:52
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
