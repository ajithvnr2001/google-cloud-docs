---
url: https://docs.cloud.google.com/alloydb/docs/alloydb-predefined-constraints/
title: Use predefined organization policies \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:24.954265+00:00
---

# Use predefined organization policies  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/alloydb-predefined-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Use predefined organization policies Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to add predefined organization policies on AlloyDB for PostgreSQL clusters and backups, which lets you put restrictions on AlloyDB at the project, folder, or organization level.

## Customer-managed encryption keys (CMEK) organization policy

You can use the CMEK organization policy to control the CMEK settings of your AlloyDB clusters and backups. This policy lets you control the [Cloud KMS keys](https://docs.cloud.google.com/kms/docs/resource-hierarchy) that you use to protect your data.

AlloyDB supports two organization policy constraints that help ensure CMEK protection across an organization:

  * `constraints/gcp.restrictNonCmekServices`: Requires CMEK protection for the `alloydb.googleapis.com`. When you add this constraint and add the `alloydb.googleapis.com` to the `Deny` policy list of services, AlloyDB refuses to create a new cluster or a backup unless they are enabled with CMEK.
  * `constraints/gcp.restrictCmekCryptoKeyProjects`: Limits which Cloud KMS CryptoKeys you can use for CMEK protection in AlloyDB clusters and backups. With this constraint, when AlloyDB creates a new cluster or a backup with CMEK, the CryptoKey must come from an allowed project, folder, or organization.



These constraints are only enforced on newly created AlloyDB clusters and backups.

For more overview information, see [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy). For information about CMEK organization policy constraints, see [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. Add the **Organization Policy Administrator** role ([`roles/orgpolicy.policyAdmin`](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy)) to your user or service account from the **IAM & Admin** page. 

[Go to the IAM accounts page](https://console.cloud.google.com/iam-admin/iam)




## Add the CMEK organization policy

To add a CMEK organization policy, follow these steps:

  1. Go to the **Organization policies** page.

[Go to the Organization policies page](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. Click the drop-down in the Google Cloud console menu bar, and then select the project, folder, or organization that requires the organization policy. The **Organization policies** page displays a list of available organization policy constraints.

  3. To set `constraints/gcp.restrictNonCmekServices`, follow these steps:

     1. Filter for the constraint using the `ID`: `constraints/gcp.restrictNonCmekServices` or the `Name`: `Restrict which services may create resources without CMEK`.
     2. Click the constraint **Name**.
     3. Click **Edit**.
     4. Click **Customize**.
     5. Click **Add rule**.
     6. Under **Policy values** , click **Custom**.
     7. Under **Policy types** , select **Deny**.
     8. Under **Custom values** , enter `alloydb.googleapis.com`. This ensures that CMEK is enforced while creating AlloyDB clusters and backups.
  4. To set `constraints/gcp.restrictCmekCryptoKeyProjects`, follow these steps:

     1. Filter for the constraint `ID`: `constraints/gcp.restrictCmekCryptoKeyProjects` or `Name`: `Restrict which projects may supply KMS CryptoKeys for CMEK`.
     2. Click the constraint **Name**.
     3. Click **Edit**.
     4. Click **Customize**.
     5. Click **Add rule**.
     6. Under **Policy values** , click **Custom**.
     7. Under **Policy types** , select **Allow**.
     8. Under **Custom values** , enter the resource using the following format: `under:organizations/ORGANIZATION_ID`, `under:folders/FOLDER_ID`, or `projects/PROJECT_ID`.

This ensures that your AlloyDB clusters and backups use the Cloud KMS keys only from the allowed project, folder, or organization.

  5. Click **Done** and then click **Save**.




## What's next

  * Learn more about [customer-managed encryption keys (CMEK) for AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/cmek).
  * See [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) to learn more about organization policies.
  * Learn more about how to [create and manage organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints).
  * See the full list of predefined [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).
  * [Connect using a public IP](https://docs.cloud.google.com/alloydb/docs/connect-public-ip).
  * [Create a primary instance](https://docs.cloud.google.com/alloydb/docs/instance-primary-create).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
