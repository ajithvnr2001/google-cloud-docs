---
url: https://docs.cloud.google.com/data-studio/enable-trusted-orgs/
title: Enable cross-organizational access with trusted orgs \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:15.257809+00:00
---

# Enable cross-organizational access with trusted orgs  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/enable-trusted-orgs/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Enable cross-organizational access with trusted orgs Stay organized with collections  Save and categorize content based on your preferences. 

This page is intended for Google Cloud organization administrators and Data Studio Pro administrators who need to enable cross-organizational user access on a self-service subscription.

To add users from external Google Cloud organizations to your Data Studio Pro subscription, contact Cloud Customer Care to enable the trusted orgs feature. Afterwards, you can assign licenses directly to individual user email addresses from those allowed domains right inside your subscription.

## Before you begin

Before you allow external users on your subscription, ensure that you meet the following requirements:

  * **Self-service subscription:** Your subscription must be self-service. Trusted organizations aren't available for organization-wide Monthly Active User (MAU) subscriptions.
  * **Support contract:** You must have an active support contract with Cloud Customer Care.
  * **Domain Restricted Sharing policy (`constraints/iam.allowedPolicyMemberDomains`):** If your organization enforces this policy, an organization administrator must navigate to **IAM & Admin > Organization Policies** in the Google Cloud console, edit `constraints/iam.allowedPolicyMemberDomains`, and add the numeric Google Workspace customer ID of each external organization to **Allowed values**. Otherwise, IAM blocks granting project or data permissions to external users or administrators.
  * **Project and data permissions:** Individual Data Studio Pro users don't need specific IAM (IAM) permissions on the project just to use Pro features or consume a license. Assigning IAM roles (such as Looker Studio Pro Manager) is required only for administrators or service accounts that manage the subscription itself. However, if external users query restricted Google Cloud data sources by using their own credentials, an administrator must grant them the appropriate data-level IAM permissions (such as BigQuery Data Viewer).



For complete role requirements, see [Data Studio Pro roles and permissions](https://docs.cloud.google.com/data-studio/about-pro-roles-and-permissions).

## Request trusted org enablement

To enable trusted organizations across your subscription, complete the following steps:

  1. Obtain the primary domain name (for example, `example.com`) and numeric Google Cloud organization ID for each organization that you want to trust. 
     * **Tip:** An administrator of the external organization can find this numeric ID inside the Google Cloud console under **IAM & Admin > Settings**. Provide the numeric Google Cloud organization ID rather than the alphanumeric Google Workspace ID.
  2. Submit a support case to [Cloud Customer Care](https://cloud.google.com/support) requesting to enable the **Trusted Orgs** feature on your Data Studio Pro subscription. Include the domain name and numeric organization ID for each trusted domain in your request.



## Important considerations

  * **Individual user assignment:** After Cloud Customer Care enables the feature, you can assign licenses to individual user email addresses from the trusted domain. You can't add Google Groups from an external organization to your subscription.
  * **Permanence:** You can't disable the trusted organizations feature after enabling it on your subscription.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
