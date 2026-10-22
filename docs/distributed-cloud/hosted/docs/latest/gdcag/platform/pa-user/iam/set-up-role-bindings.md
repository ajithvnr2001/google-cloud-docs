---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings/
title: Grant and revoke access \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:51.423953+00:00
---

# Grant and revoke access  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Grant and revoke access Stay organized with collections  Save and categorize content based on your preferences. 

Every subject - a user or a group - follows a two-step process to gain access to the global API server. Grant a subject with permissions in the global API server using `IAMRoleBinding` to a predefined `IAMRole`. All role and role bindings are global.

**Note:** You can bind one subject to multiple roles in the global API server and Kubernetes clusters. Permissions are purely additive, and there are no deny rules.

This page is for audiences within the platform administrator group who manage permissions within their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

Before managing role bindings or revoking access, you must request the necessary permissions and prepare your environment. The specific roles required depend on whether you are managing role bindings or revoking user access.

### Request IAM roles

Contact your IAM Org Admin to request the roles based on the tasks you need to perform:

  * **IAM Org Admin** (`organization-iam-admin`): create, update, and delete role bindings at the organization and project levels.
  * **Org Session Admin** (`org-session-admin`): revoke a user's active sessions and access within a specific zone.



### Prepare your environment

To use the command-line tools for managing role bindings or revoking access, complete the following setup.

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.
  * To use the API with `kubectl`, additional setup is required: 
    * [Install the kubectl CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl).
    * [Generate the kubeconfig file for the global API server](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig).



## Set up role bindings

You can set up role bindings that give team members access to resources at the organization or project level.

Assign a role to an authorized member:

###  Console 

  1. Sign in to the GDC console.
  2. Select an organization or project from the scope picker. 
     * To set up role bindings for an organization, select an organization.
     * To set up role bindings for a project, select a project.
  3. In the navigation menu, click **Identity and Access > Access**.
  4. Click **Add Member**.
  5. Choose whether you want to add individual users or groups.
  6. In the **Identity provider** list, select an identity provider.
  7. In the **Username or group alias** field, enter the username, email address, or alias.
  8. In the **Role** list, select the role that you want to assign to the user or group, such as **Organization Viewer** at the organization level or **Project Creator** at the project level.
  9. Click **Add**.



The member appears in the **Authorized member** list.

###  gdcloud 

  1. Ensure you have the [gdcloud CLI installed](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview#download-and-install).

  2. Sign in using the `gdcloud auth login` command to authenticate with your identity provider. For more information, see [the gdcloud CLI authentication](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth#login).

  3. Set up role bindings.

     * Set up role bindings for an organization:
           
           gdcloud organizations add-iam-policy-binding ORGANIZATION \
             --member=USER_ACCOUNT \
             --role=ROLE
           

Replace the following variables:

       * `ORGANIZATION`: the name of the organization for which you're setting up the role binding.
       * `USER_ACCOUNT`: the user account to which you want to grant the role. This flag accepts either a user email address with the identity provider prefix (`user:idpprefix-user@example.com`) or a service account name with the service account project (`serviceAccount:projectName:serviceAccountName`).
       * `ROLE`: the name of the predefined or custom role you want to assign to the user.
     * Set up role bindings for a project:
           
           gdcloud projects add-iam-policy-binding PROJECT \
             --member=USER_ACCOUNT \
             --role=ROLE
           

Replace the following variables:

       * `PROJECT`: the name of the project for which you're setting up the role binding.
       * `USER_ACCOUNT`: the user account to which you want to grant the role. This flag accepts either a user email address with the identity provider prefix (`user:idpprefix-user@example.com`) or a service account name with the service account project (`serviceAccount:projectName:serviceAccountName`).
       * `ROLE`: the name of the predefined or custom role you want to assign to the user.



###  API 

  1. Export the environment variables for the role binding:
         
         export GLOBAL_API_SERVER_KUBECONFIG=GLOBAL_API_SERVER_KUBECONFIG
         export USERNAME=IDP_PREFIX-USERNAME
         export ROLE_NAME=ROLE_NAME
         export BINDING_NAMESPACE=BINDING_NAMESPACE
         export USER_EMAIL=IDP_PREFIX-USER_EMAIL
         

Replace the following:

     * `GLOBAL_API_SERVER_KUBECONFIG`: the path to the kubeconfig file for the global API server.
     * `IDP_PREFIX`: the identity provider prefix.
     * `USERNAME`: the username portion of the user's email address before the `@` symbol (such as `paul` from `paul@example.com`).
     * `ROLE_NAME`: the name of the role the user needs (such as `project-creator`). See [Role definitions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/role-definitions) for a list of roles and their scope.
     * `BINDING_NAMESPACE`: `platform` for organization-scoped roles, or the name of the target project's namespace for project-scoped roles.
     * `USER_EMAIL`: the email address of the user account for which you want to assign the role (such as `paul@example.com`).
  2. Create and apply an `IAMRoleBinding` custom resource:
         
         cat <<EOF | kubectl --kubeconfig ${GLOBAL_API_SERVER_KUBECONFIG} apply -f -
         apiVersion: iam.global.gdc.goog/v1
         kind: IAMRoleBinding
         metadata:
           name: ${USERNAME}-${ROLE_NAME}-binding
           namespace: ${BINDING_NAMESPACE}
         spec:
           roleRef:
             apiGroup: iam.global.gdc.goog
             kind: IAMRole
             name: ${ROLE_NAME}
           subjects:
           - apiGroup: rbac.authorization.k8s.io
             kind: User
             name: ${USER_EMAIL}
         EOF
         




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

  1. Ensure you have the [gdcloud CLI installed](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview#download-and-install).

  2. Sign in using the `gdcloud auth login` command to authenticate with your identity provider. For more information, see [the gdcloud CLI authentication](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth#login).

  3. Remove role bindings.

     * Remove role bindings for an organization:
           
           gdcloud organizations remove-iam-policy-binding ORGANIZATION \
             --member=USER_ACCOUNT \
             --role=ROLE
           

Replace the following variables:

       * `ORGANIZATION`: the name of the organization from which you're removing the role binding.
       * `USER_ACCOUNT`: the user account from which you want to remove the role. This flag accepts either a user email address with the identity provider prefix (`user:idpprefix-user@example.com`) or a service account name with the service account project (`serviceAccount:projectName:serviceAccountName`).
       * `ROLE`: the name of the predefined or custom role you want to remove from the user account.
     * Remove role bindings for a project:
           
           gdcloud projects remove-iam-policy-binding PROJECT \
             --member=USER_ACCOUNT \
             --role=ROLE
           

Replace the following variables:

       * `PROJECT`: the name of the project from which you're removing the role binding.
       * `USER_ACCOUNT`: the user account from which you want to remove the role. This flag accepts either a user email address with the identity provider prefix (`user:idpprefix-user@example.com`) or a service account name with the service account project (`serviceAccount:projectName:serviceAccountName`).
       * `ROLE`: the name of the predefined or custom role you want to remove from the user account.



### kubectl

Delete the `IAMRoleBinding` to revoke the permission granted to the PA account:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER_KUBECONFIG \
    delete iamrolebinding IDP_PREFIX-USERNAME-ROLE_NAME-binding -n BINDING_NAMESPACE
    

Replace the following:

  * GLOBAL_API_SERVER_KUBECONFIG: the path to the kubeconfig file for the global API server.
  * IDP_PREFIX: the identity provider prefix.
  * USERNAME: the username portion of the user's email address before the `@` symbol (such as `paul` from `paul@example.com`).
  * ROLE_NAME: the name of the role you want to remove, such as `project-creator`.
  * BINDING_NAMESPACE: replace with `platform` for organization-scoped roles, or the name of the target project's namespace for project-scoped roles.



## Revoke user access

If a member leaves your organization or team, you can revoke their access to Google Distributed Cloud (GDC) air-gapped. Revoking a user's access logs them out of Distributed Cloud and removes their roles and permissions. You can also list the user's activity and sessions from their start and end time.

To revoke a user's access across a GDC universe, you must revoke access for each individual zone separately. Complete the following steps for each zone:

  1. Ensure you are signed in to the zone you want to revoke access for. For example, set the zonal URL configuration for gdcloud CLI, and then sign in:
         
         gdcloud config set organization_console_url ZONE_URL
         gdcloud auth login
         

Replace `ZONE_URL` with the GDC console URL for the zone to revoke user access for, which resembles `https://console.ORG_NAME.ZONE_NAME.ORG_SUFFIX`.

For more information about switching zonal contexts, see [Access zones with your tools](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/access-zones).

  2. Revoke the user's access for the zone:
         
         gdcloud admin auth revoke --accounts USER_EMAIL
         

Replace USER_EMAIL with the email of the user to revoke access.

After running the command, you see output similar to the following. This example revokes access from the user `ariel@example.com`:
         
         Success: NUMBER of sessions revoked for user ariel@example.com
         

In this example, the variable NUMBER refers to the number of active sessions the user had.

  3. Confirm you've revoked the user's access by running the `gdcloud admin auth revoke` command again. If successful, you see the following:
         
         No sessions found for account: ariel@example.com
         

  4. Repeat the previous steps for each zone in your universe.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
