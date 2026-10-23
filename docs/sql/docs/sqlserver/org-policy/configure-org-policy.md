---
url: https://docs.cloud.google.com/sql/docs/sqlserver/org-policy/configure-org-policy/
title: Add predefined organization policies \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:08.795313+00:00
---

# Add predefined organization policies  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/org-policy/configure-org-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Add predefined organization policies Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/org-policy/configure-org-policy "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/org-policy/configure-org-policy "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to add organization policies on Cloud SQL instances, to put restrictions on Cloud SQL at the project, folder, or organization level. For an overview, see [Cloud SQL organization policies](https://docs.cloud.google.com/sql/docs/sqlserver/org-policy/org-policy).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

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

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. Add the **Organization Policy Administrator** role ([`roles/orgpolicy.policyAdmin`](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy)) to your user or service account from the **IAM & Admin** page. 

[Go to the IAM accounts page](https://console.cloud.google.com/iam-admin/iam)

  13. See [Restrictions](https://docs.cloud.google.com/sql/docs/sqlserver/org-policy/org-policy#restrictions) before performing this procedure.



## Add the connection organization policy

For an overview see [Connection organization policies](https://docs.cloud.google.com/sql/docs/sqlserver/org-policy/org-policy#connection-organization-policy).

To add a connection organization policy:

  1. Go to the **Organization policies** page.

[Go to the Organization policies page](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. Click projects dropdown menu in the top tab, and then select the project, folder, or organization that requires the organization policy. The **Organization policies** page displays a list of organization policy constraints that are available.

  3. Filter for the constraint `name` or `display_name`.

     * To disable access to or from the Internet:
           
           name: "constraints/sql.restrictPublicIp"
           display_name: "Restrict Public IP access on Cloud SQL instances"
           

     * To disable access from the internet when IAM authentication is missing (this does not affect access using Private IP):
           
           name: "constraints/sql.restrictAuthorizedNetworks"
           display_name: "Restrict Authorized Networks on Cloud SQL instances"
           

  4. Select the policy **Name** from the list.

  5. Click **Edit**.

  6. Click **Customize**.

  7. Click **Add rule**.

  8. Under **Enforcement** , click **On**.

  9. Click **Save**.




## Add the CMEK organization policy

For an overview, see [Customer-managed encryption keys organization policies](https://docs.cloud.google.com/sql/docs/sqlserver/org-policy/org-policy#cmek-organization-policy).

To add a CMEK organization policy:

  1. Go to the **Organization policies** page.

[Go to the Organization policies page](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. Click projects dropdown menu in the top tab, and then select the project, folder, or organization that requires the organization policy. The **Organization policies** page displays a list of organization policy constraints that are available.

  3. Filter for the constraint `name` or `display_name`.

     * To put service names in a DENY list to ensure that CMEK is used in the resources for that service:
           
           name: "constraints/gcp.restrictNonCmekServices"
           display_name: "Restrict which services may create resources without CMEK"
           

You must add `sqladmin.googleapis.com` to the list of restricted services with Deny.

     * To put project IDs in an ALLOW list to ensure that only keys from an instance of Cloud KMS within that project are used for CMEK.
           
           name: "constraints/gcp.restrictCmekCryptoKeyProjects"
           display_name: "Restrict which projects may supply KMS CryptoKeys for CMEK"
           

  4. Select the policy **Name** from the list.

  5. Click **Edit**.

  6. Click **Customize**.

  7. Click **Add rule**.

  8. Under **Policy values** , click **Custom**.

  9. For `constraints/gcp.restrictNonCmekServices`: a. Under **Policy types** , select **Deny**. b. Under **Custom values** , enter `sqladmin.googleapis.com`.

For `constraints/gcp.restrictCmekCryptoKeyProjects`: a. Under **Policy types** , select **Allow**. b. Under **Custom values** , enter the resource using the following format: `under:organizations/ORGANIZATION_ID`, `under:folders/FOLDER_ID`, or `projects/PROJECT_ID`.

  10. Click **Done**.

  11. Click **Save**.




## What's next

  * Learn about [Organization policies](https://docs.cloud.google.com/sql/docs/sqlserver/org-policy/org-policy).
  * Learn about how [private IP](https://docs.cloud.google.com/sql/docs/sqlserver/private-ip) works with Cloud SQL.
  * Learn how to [configure private IP](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip) for Cloud SQL.
  * Learn about the [organization policy service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).
  * Learn about [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
