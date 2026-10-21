---
url: https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access/
title: Grant users instance access \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:22.419225+00:00
---

# Grant users instance access  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Grant users instance access Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to grant your users access to your Secure Source Manager instance using Identity and Access Management (IAM). For more details on access control in Secure Source Manager, see [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control)

## Required roles

To get the permissions that you need to grant users instance access, ask your administrator to grant you the [Secure Source Manager Instance Owner role ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`) IAM role on the Secure Source Manager instance. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For information on granting Secure Source Manager roles, see [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control).

## Grant Workforce Identity Federation users access

If you use Workforce Identity Federation to access Secure Source Manager, then principals are represented differently. To learn more about granting access to principals that represent groups of identities, see [Represent workforce pool users in IAM policies](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#representing-workforce-users).

For example, the following command grants the user `user@example.com` the Instance Accessor role (`roles/securesourcemanager.instanceAccessor`) in the workforce pool `my-pool` on the instance `my-instance` in the project `my-project` in the `us-central1` region:
    
    
      gcloud source-manager instances add-iam-policy-binding my-instance \
          --project=my-project \
          --region=us-central1 \
          --member=principal://iam.googleapis.com/locations/global/workforcePools/my-pool/subject/user@example.com \
          --role=roles/securesourcemanager.instanceAccessor
    

You can grant users or groups within your workforce identity pool based on your Identity provider (IdP) attributes, or use [Common Expression Language (CEL)](https://github.com/google/cel-spec) to map your OIDC attributes to custom attributes to define an authorization strategy in your IAM policy. For more information about attribute mappings, read [Attribute mappings](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings).

## Grant instance access in the Google Cloud console

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector2/iam-admin/iam?supportedpurview=project)

  2. Click **Grant access**.

  3. In the **New principals** field, enter the email address of the user or group you want to grant access to.

  4. Select a role from the **Select a role** list.

     * To grant view-only access to the instance, select **Secure Source Manager Instance Accessor** (`roles/securesourcemanager.instanceAccessor`). This role grants access to the instance, but does not grant repository view permissions.
     * To grant read-only access to repositories, select **Secure Source Manager Repository Reader** (`roles/securesourcemanager.repoReader`). Users also need the Instance Accessor role to access repositories through the Secure Source Manager web interface.
     * To allow creating and modifying repositories, select **Secure Source Manager Instance Repository Creator** (`roles/securesourcemanager.instanceRepositoryCreator`).
     * To grant full administrative access to the instance, select **Secure Source Manager Instance Owner** (`roles/securesourcemanager.instanceOwner`).
  5. Click **Save**.




## Grant a single user access

To grant a single user access to the instance use the following Google Cloud CLI command:
    
    
      gcloud source-manager instances add-iam-policy-binding INSTANCE_ID \
          --project=PROJECT_ID \
          --region=REGION \
          --member=PRINCIPAL_IDENTIFIER \
          --role=roles/securesourcemanager.instanceAccessor
    

Replace the following:

  * `INSTANCE_ID` with the instance ID.
  * `PROJECT_ID` with the project ID or project number of the instance.
  * `REGION` with the region the instance is located in. See the [locations documentation](https://docs.cloud.google.com/secure-source-manager/docs/locations) for available Secure Source Manager regions.
  * `PRINCIPAL_IDENTIFIER` with the identifier for the principal you want to grant the role to.

For example, to grant the role to a single user with their email address, you would format the principal identifier as `user:EMAIL` where EMAIL is the email address of the user.

For more information on supported principal identifiers, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).




For example, the following command grants the `trusted-user1@gmail.com` user the `roles/securesourcemanager.instanceAccessor` role on the instance `my-instance`, in the project `my-project` in the `us-central` region.
    
    
      gcloud source-manager instances add-iam-policy-binding INSTANCE_ID \
          --project=my-project \
          --region=us-central1 \
          --member=user:trusted-user1@gmail.com \
          --role=roles/securesourcemanager.instanceAccessor
    

## Grant multiple users access

To grant access to multiple users, we recommend creating a [Google group](https://support.google.com/a/answer/9400082) that includes all potential users, such as all developers.

You can then grant the group one or more of the following roles:

  * **Instance Accessor** (`roles/securesourcemanager.instanceAccessor`): View the instance.
  * **Instance Repository Creator** (`roles/securesourcemanager.instanceRepositoryCreator`): Create and modify repositories.
  * **Instance Owner** (`roles/securesourcemanager.instanceOwner`): Full management of the instance.



For instructions on how to grant roles to a group, see [Granting access to multiple principals](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#multiple-roles-programmatic) in the IAM documentation.

## What's next

  * [Grant users repository access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-repository-access).
  * Learn more about [access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control).
  * [Create a repository](https://docs.cloud.google.com/secure-source-manager/docs/create-repository).
  * [Grant and revoke IAM roles](https://docs.cloud.google.com/secure-source-manager/docs/update-iam-policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
