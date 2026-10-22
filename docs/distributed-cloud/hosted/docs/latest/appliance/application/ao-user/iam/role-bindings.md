---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/role-bindings/
title: Grant access to project resources \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:42.382887+00:00
---

# Grant access to project resources  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/role-bindings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Grant access to project resources Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to create and remove role bindings within a GDC air-gapped appliance project using the GDC console or the gdcloud CLI.

## Before you begin

Before creating or removing role bindings, you must request the necessary permissions.

### Request IAM roles

To create, update, and delete role bindings within a project, contact your Organization IAM Admin or Project IAM Admin to request the **Project IAM Admin** (`project-iam-admin`) role.

The Organization IAM Admin can grant this role for any project within the organization. The Project IAM Admin can grant this role within the scope of their specific project.

## Set up role bindings

Work through the following steps to set up role bindings:

###  Console 

  1. Sign in to the GDC air-gapped appliance console. For example, the following image signs in to the GDC console for an organization named `org-1`: ![](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/images/login.png)
  2. Click **Select project** in the menu bar. Select one of the existing projects you want to set up the role binding in, then click **Open**. The selected project displays after your org name in the menu bar. The following example shows the selected `iam-test` project: ![](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/images/select-project.png)
  3. In the navigation menu, click **Identity & Access** and **Access**.
  4. Click **Add member**. ![](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/images/add-member.png)
  5. In the **Identity provider** dropdown menu, select an identity provider.
  6. After **Member type** , choose whether you want to add individual users with **User** , or groups with **Group**. The following example shows **User** selected: ![](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/images/member-type.png)
  7. In the **Username or group alias** field, enter the username, email address, or alias. ![](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/images/username-or-group-alias.png)
  8. In the **Roles** drop-down list, select the role that you want to assign to the user or group, such as **Project Viewer**. You can bind the selected user or group with multiple roles at a time by clicking **Add Another Role**. ![](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/images/role.png)
  9. Click **Add**.



###  gdcloud 

  1. Ensure you have the [gdcloud CLI installed](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview#download-and-install).

  2. Sign in using the `gdcloud auth login` command to authenticate with your identity provider. For more information, see [the gdcloud CLI authentication](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-auth#login).

  3. Set up role bindings for a project:
         
         gdcloud projects add-iam-policy-binding PROJECT \
           --member=USER_ACCOUNT \
           --role=ROLE
         

Replace the following variables:

     * `PROJECT`: the name of the project for which you're setting up the role binding.
     * `USER_ACCOUNT`: the user account to which you want to grant the role. This flag accepts either a user email address with the identity provider prefix (`user:idpprefix-user@example.com`) or a service account name with the service account project (`serviceAccount:projectName:serviceAccountName`).
     * `ROLE`: the name of the predefined or custom role you want to assign to the user.



## Remove role bindings

When access is no longer required, remove a member and their associated roles, permissions, and access.

To remove members, work through the following steps:

###  Console 

  1. Sign in to the GDC air-gapped appliance console.
  2. Click **Select project** in the menu bar. Select one of the existing projects you want to set up the role binding in, then click **Open**. The selected project displays after your org name in the menu bar.
  3. In the navigation menu, click **Identity & Access** and **Access**.
  4. In the authorized members list, select a member. You can remove multiple members at a time by selecting multiple members in the list. ![](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/images/members.png)
  5. Click **Remove All Access** to remove all the role bindings associated with a member from your current project. ![](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/images/remove-all-access.png)
  6. When prompted, click **Remove Member** to confirm. ![](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/images/remove-member.png)



###  gdcloud 

  1. Ensure you have the [gdcloud CLI installed](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview#download-and-install).

  2. Sign in using the `gdcloud auth login` command to authenticate with your identity provider. For more information, see [the gdcloud CLI authentication](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-auth#login).

  3. Remove role bindings for a project:
         
         gdcloud projects remove-iam-policy-binding PROJECT \
           --member=USER_ACCOUNT \
           --role=ROLE
         

Replace the following variables:

     * `PROJECT`: the name of the project from which you're removing the role binding.
     * `USER_ACCOUNT`: the user account from which you want to remove the role. This flag accepts either a user email address with the identity provider prefix (`user:idpprefix-user@example.com`) or a service account name with the service account project (`serviceAccount:projectName:serviceAccountName`).
     * `ROLE`: the name of the predefined or custom role you want to remove from the user account.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
