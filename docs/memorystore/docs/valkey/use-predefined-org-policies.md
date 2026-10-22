---
url: https://docs.cloud.google.com/memorystore/docs/valkey/use-predefined-org-policies/
title: Ensure customer-managed encryption key (CMEK) protection for your instances by using predefined organization policy constraints \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:56.527976+00:00
---

# Ensure customer-managed encryption key (CMEK) protection for your instances by using predefined organization policy constraints  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/use-predefined-org-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Ensure customer-managed encryption key (CMEK) protection for your instances by using predefined organization policy constraints Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use [predefined organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints) for Memorystore for Valkey. These constraints let you put restrictions on Memorystore for Valkey at the project, folder, or organization level.

You can use organization policy constraints to help ensure customer-managed encryption key (CMEK) protection for your Memorystore for Valkey instances by controlling the CMEK settings of the instances. As a result, you not only can enforce CMEK protection for your instances, but you also can control which [Cloud Key Management Service (KMS) keys](https://docs.cloud.google.com/kms/docs/resource-hierarchy) you can use to help protect your data.

Organization policy constraints are enforced only on newly created Memorystore for Valkey instances. For more information, see [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy) and [Organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).

## Before you begin

Before you begin to use predefined organization policy constraints, complete the prerequisites in this section.

### Use the Google Cloud console, Google Cloud CLI, and APIs

To use the Google Cloud console, gcloud CLI, and APIs, do the following:

  1. In the Google Cloud console, on the project selector page, select or [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

[Go to the project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Make sure that billing is enabled for your project. Learn how to [check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).
  3. [Install](https://docs.cloud.google.com/sdk/docs/install) and [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the Google Cloud CLI (gcloud CLI).

If you installed the gcloud CLI, then make sure you have the latest version by running `gcloud components update`. To access the Memorystore for Valkey gcloud CLI commands, you need at least gcloud CLI version `489.0.0`.

  4. Enable the Memorystore for Valkey API.   
[Memorystore for Valkey API](https://console.cloud.google.com/apis/library/memorystore.googleapis.com)
  5. If you're using an external identity provider (IdP), then you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).
  6. Make sure that you know your organization's [ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).



### Assign roles

To use predefined organization policy constraints for your instances, you must have one of these [IAM roles](https://docs.cloud.google.com/memorystore/docs/valkey/access-control) in your Google Cloud project:

  * `roles/memorystore.admin` (the Memorystore Admin role)
  * `roles/owner` (the Owner role)
  * `roles/editor` (the Editor role)



In addition, you must grant the [`roles/orgpolicy.policyAdmin`](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (Organization Policy Administrator) role to your user or service account. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You might also get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined).

## Add predefined CMEK constraints to an organization policy

In this section, you add the following predefined CMEK constraints to an organization policy:

  * `constraints/gcp.restrictNonCmekServices`: enforces CMEK protection for your instances. If the [Memorystore for Valkey API](https://docs.cloud.google.com/kms/docs/cmek-org-policy) is in the `Deny` policy list of services for this constraint, then you can't create non-CMEK-protected instances.
  * `constraints/gcp.restrictCmekCryptoKeyProjects`: limit which Cloud KMS keys you can use for CMEK protection. If you configure this constraint, then the instances that use CMEK encryption must use a key from an allowed project, folder, or organization.



To add these CMEK constraints to an organization policy, do the following:

  1. Go to the **Organization policies** page.

[Go to the Organization policies page](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. Click the menu in the Google Cloud console menu bar, and then select the project, folder, or organization that requires the organization policy.

On the **Organization policies** page, a list of available organization policy constraints is displayed.

  3. To set the `constraints/gcp.restrictNonCmekServices` constraint, follow these steps:

     1. Filter for the constraint by using its ID: `constraints/gcp.restrictNonCmekServices`.
     2. Click the link that contains the constraint's name.
     3. On the **Policy details** page, click **Manage policy**.
     4. In the **Policy source** section of the **Edit policy** page, click the **Override parent's policy** option.
     5. In the **Rules** section, click the **Add a rule** field.
     6. From the **Policy values** menu of the **New rule** dialog, select **Custom**.
     7. From the **Policy type** menu, select **Deny**.
     8. In the **Custom values** field, enter `memorystore.googleapis.com`. This value enforces CMEK protection when you create Memorystore for Valkey instances.
     9. Click **Set policy**.
  4. To set the `constraints/gcp.restrictCmekCryptoKeyProjects` constraint, follow these steps:

     1. Filter for the constraint by using its ID: `constraints/gcp.restrictCmekCryptoKeyProjects`.
     2. Click the link that contains the constraint's name.
     3. On the **Policy details** page, click **Manage policy**.
     4. In the **Policy source** section of the **Edit policy** page, click the **Override parent's policy** option.
     5. In the **Rules** section, click the **Add a rule** field.
     6. From the **Policy values** menu of the **New rule** dialog, select **Custom**.
     7. From the **Policy type** menu, select **Allow**.
     8. In the **Custom values** field, enter the resource using the following format: `under:organizations/ORGANIZATION_ID`, `under:folders/FOLDER_ID`, or `projects/PROJECT_ID`.

These values let Memorystore for Valkey instances use Cloud KMS keys only from the allowed organization, folder, or project.

     9. Click **Set policy**.




## What's next

  * Learn more about [(CMEK) for Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey/about-cmek).
  * Learn more about [organization policies](https://docs.cloud.google.com/organization-policy/overview).
  * Learn more about [creating organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies).
  * View the full list of predefined [organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
