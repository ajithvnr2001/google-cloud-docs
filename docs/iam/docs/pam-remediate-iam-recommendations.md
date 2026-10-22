---
url: https://docs.cloud.google.com/iam/docs/pam-remediate-iam-recommendations/
title: Remediate excessive permissions with Privileged Access Manager \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:20.502193+00:00
---

# Remediate excessive permissions with Privileged Access Manager  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/pam-remediate-iam-recommendations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Remediate excessive permissions with Privileged Access Manager Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If the IAM recommender identifies that a principal has excessive permissions, you can remediate the finding by transitioning the principal's permanent role binding to a temporary, on-demand entitlement in Privileged Access Manager (PAM).

This approach lets you achieve a [least privilege posture](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) without the risk of permanently revoking access that might be needed for infrequent but critical tasks.

## Before you begin

  1. Ensure that Privileged Access Manager is [onboarded and enabled](https://docs.cloud.google.com/iam/docs/pam-permissions-and-setup) for the resource (project, folder, or organization) where the role is granted.
  2. Verify that you have the permissions required to complete this guide.



### Required roles and permissions

To get the permissions that you need to complete the tasks in this guide, ask your administrator to grant you the following IAM roles on your Google Cloud project: 

  * To view role recommendations: 
    * [Recommender IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.iamAdmin) (`roles/recommender.iamAdmin`)
    * [Recommender IAM Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.iamViewer) (`roles/recommender.iamViewer`)
  * To create Privileged Access Manager (PAM) entitlements: 
    * [Privileged Access Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)
    * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to complete the tasks in this guide. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to complete the tasks in this guide:

  * To view role recommendations: 
    * `recommender.iamPolicyInsights.list`
    * `recommender.iamPolicyRecommendations.list`
    * `resourcemanager.projects.get`
  * To create PAM entitlements: 
    * `privilegedaccessmanager.entitlements.create`
    * `privilegedaccessmanager.entitlements.list`
    * `privilegedaccessmanager.locations.list`
    * `privilegedaccessmanager.locations.get`
    * `resourcemanager.projects.get`
    * `resourcemanager.projects.setIamPolicy`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Transition a role to a Privileged Access Manager entitlement

When you transition a role to a Privileged Access Manager entitlement, IAM recommender coordinates with Privileged Access Manager to create an entitlement and remove the original permanent role binding. You can do this from either the **Security Insights** page or the **IAM** page in the Google Cloud console.

###  Security Insights 

To transition a role from the **Security Insights** page, do the following:

  1. In the Google Cloud console, go to the **IAM & Admin > Security Insights** page.

[Go to Security Insights](https://console.cloud.google.com/iam-admin/security-insights)

  2. Locate the **Top groups with excess permissions** widget.

  3. For the group that you want to remediate permissions for, click the corresponding link in the **Insights** column.

  4. For the insight type that you want to address, click **View recommendation**.

  5. In the **Overview** page, select **Remove role and grant on-demand access to the role**.

  6. To create an entitlement with the required role, enter the required details, and click **Apply**. The **Role** and **Resource** fields in the form are pre-populated based on the recommendation. The **Duration** defaults to 8 hours. For detailed instructions, see [Create entitlements](https://docs.cloud.google.com/iam/docs/pam-create-entitlements#create-entitlements).

Privileged Access Manager creates a new entitlement based on your configuration and removes the permanent role binding from the resource's allow policy.

Access changes take 1–2 minutes to take effect.




###  IAM 

To transition a role from the **IAM** page, do the following:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. In the list of principals, locate the group that you want to remediate permissions for.

  3. To view recommendations for that group principal, click the insight in the **Security insights** column.

  4. In the **Overview** page, select **Remove role and grant on-demand access to the role**.

  5. To create an entitlement with the required role, enter the required details, and click **Apply**. The **Role** and **Resource** fields in the form are pre-populated based on the recommendation. The **Duration** defaults to 8 hours. For detailed instructions, see [Create entitlements](https://docs.cloud.google.com/iam/docs/pam-create-entitlements#create-entitlements).

Privileged Access Manager creates a new entitlement based on your configuration and removes the permanent role binding from the resource's allow policy.

Access changes take 1–2 minutes to take effect.




## Revert a recommendation

To revert a recommendation, see [Revert recommendations](https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations#history).

After you revert the recommendation, the system restores the original IAM binding and deletes the created Privileged Access Manager entitlement.

**Note:** If the revert process fails, then [delete the entitlement manually](https://docs.cloud.google.com/iam/docs/pam-view-update-delete-entitlements).

## What's next

  * Learn more about [role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview).
  * Understand [PAM entitlements](https://docs.cloud.google.com/iam/docs/pam-create-entitlements).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
