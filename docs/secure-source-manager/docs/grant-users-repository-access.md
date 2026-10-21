---
url: https://docs.cloud.google.com/secure-source-manager/docs/grant-users-repository-access/
title: Grant users repository access \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:41.139575+00:00
---

# Grant users repository access  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/grant-users-repository-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Grant users repository access Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to grant repository-level roles to users, groups, and service accounts in the Secure Source Manager web interface.

For information on which roles to grant for a certain use-case, see [Repository role management](https://docs.cloud.google.com/secure-source-manager/docs/access-control#repository_role_management).

## Required roles

To get the permissions that you need to grant users repository-level roles, ask your administrator to grant you the following IAM roles: 

  * [Secure Source Manager Instance Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceAccessor) (`roles/securesourcemanager.instanceAccessor`) on the Secure Source Manager instance
  * [Secure Source Manager Repo Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`) on the repository



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For information on granting Secure Source Manager roles, see [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control) and [Grant users instance access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access).

## Grant users repository-level roles

Users, groups, and service accounts must be granted the Instance Accessor role (`roles/securesourcemanager.instanceAccessor`) or Instance Repository Creator role (`roles.securesourcemanager.instanceRepositoryCreator`) before they can be granted repository roles. For information on granting instance roles, see [Grant or revoke instance access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access).

If you're authenticating to Secure Source Manager using a third-party identity provider and Workforce Identity Federation, then principals must be added to your workforce identity pool, and granted at least the Instance Accessor role (`roles/securesourcemanager.instanceAccessor`). For information about managing workforce identity pools, see [Manage workforce identity pools and providers](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers).

You can use the Secure Source Manager API or the Secure Source Manager web interface to grant users, groups, and service accounts repository-level roles. For more information, see [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control).

To grant users or service accounts repository-level roles using the web interface:

  1. To access the Secure Source Manager instance through its web interface, copy the following URL into your browser address bar.
         
         INSTANCE_ID-PROJECT_NUMBER.LOCATION.sourcemanager.dev

Replace the following: 

     * INSTANCE_ID with the instance name.
     * PROJECT_NUMBER with the instance's Google Cloud project number. For information on identifying projects, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * LOCATION with the instance's region.
  2. From the **My repositories** page, Select your repository.
  3. Click the **Permissions** tab.
  4. In the **People and permissions** section, click **Add users**.
  5. In the **Add principal** field, enter the email of the user or service account you want to grant the role to.
  6. In the **Assign a role** menu, select the role to assign.
  7. Click **Save**.



To add additional roles click the edit **Edit** icon and add the roles using the **Assign a role** menu.

## What's next

  * [Use Git source code management](https://docs.cloud.google.com/secure-source-manager/docs/use-git) with Secure Source Manager.
  * Learn more about [access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control).
  * [Grant and revoke IAM roles](https://docs.cloud.google.com/secure-source-manager/docs/update-iam-policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
