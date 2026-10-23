---
url: https://docs.cloud.google.com/data-studio/about-pro-roles-and-permissions/
title: Data Studio Pro roles and permissions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:49.456955+00:00
---

# Data Studio Pro roles and permissions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/about-pro-roles-and-permissions/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Data Studio Pro roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

Data Studio Pro uses Identity and Access Management (IAM) to manage administrative access, subscriptions, and licenses. Predefined IAM roles let you delegate project-level and organization-wide administration without configuring individual permissions manually.

Don't have a subscription yet? [Subscribe to Data Studio Pro](https://docs.cloud.google.com/data-studio/pro-subscription-overview).

## Overview of Data Studio Pro administration

Data Studio Pro uses IAM to control who can manage subscriptions, assign licenses, and link Google Cloud projects. Unlike Data Studio content-level roles (such as Viewer or Editor roles on a specific report or data source), IAM management roles control organization-wide and project-level administrative tasks.

For standard self-service subscriptions, you manage permissions directly on the Google Cloud project that's associated with your subscription. For org-wide Monthly Active User (MAU) subscriptions, you manage administrative privileges through your Google Workspace Admin console.

## Predefined IAM roles

You can use predefined IAM roles to grant access to Data Studio Pro administrative features without needing to configure individual permissions manually.

The following table describes the primary roles that you use to administer Data Studio Pro subscriptions:

Role | Permissions | Description  
---|---|---  
Owner  
(`roles/owner`) | Full access to all Google Cloud resources and permissions, including `resourcemanager.projects.updateLiens` and `lookerstudio.pro.manage`. | Recommended for project creators and primary administrators who need to link existing Google Cloud projects, start new subscriptions, and manage ongoing license assignments.  
Looker Studio Pro Manager  
(`roles/lookerstudio.proManager`) | Includes `lookerstudio.pro.manage`, `resourcemanager.projects.get`, `resourcemanager.projects.list`, and `resourcemanager.projects.updateLiens`. | Dedicated predefined role for Data Studio Pro administrators. Grants all permissions required to start new subscriptions, manage users, adjust licenses, and protect project assets without granting wider project ownership.  
Project Lien Modifier  
(`roles/resourcemanager.lienModifier`) | Includes `resourcemanager.projects.updateLiens`, `resourcemanager.projects.get`, and `resourcemanager.projects.list`. | Used to create and delete project safety [liens](https://docs.cloud.google.com/resource-manager/docs/project-liens) that prevent accidental deletion of Data Studio Pro assets. Doesn't grant permission to manage Data Studio Pro users or licenses.  
  
For more information about Cloud IAM roles, see [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

## Granular permissions and custom roles

If your organization enforces the [principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely), you can create [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) that are tailored to specific administrative workflows. The granular permissions that are required depend on whether an administrator creates a new subscription or manages an existing subscription.

### Create a new subscription

To start a new self-service Data Studio Pro subscription or link a new project, a custom role must include the following permissions:

  * `lookerstudio.pro.manage` — Lets you create and configure the Pro subscription.
  * `resourcemanager.projects.get` — Required to verify project metadata and billing status.
  * `resourcemanager.projects.list` — Lets you select the Google Cloud project in the console interface.
  * `resourcemanager.projects.updateLiens` — Lets Google Cloud place a safety [lien](https://docs.cloud.google.com/resource-manager/docs/project-liens) on the project when you subscribe, which prevents accidental deletion of your organization's Data Studio Pro assets.



### Manage an existing subscription

For administrators whose sole responsibility is managing day-to-day user membership and adjusting license totals on an already active subscription, you don't need to modify project safety liens. A custom management role requires only the following permissions:

  * `lookerstudio.pro.manage`
  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`

**Note:** The `resourcemanager.projects.updateLiens` permission is required only when creating a subscription; it isn't required for day-to-day user and license management. 

## Manage org-wide MAU subscriptions

To manage an organization-wide Monthly Active User (MAU) subscription, you must be signed in as a Google Workspace user who has a role that contains the Manage Data Studio Settings Google Workspace privilege.

This privilege is included in the predefined Workspace Services Admin and Workspace Super Admin roles. You can also grant this privilege by using a [custom Admin role](https://support.google.com/a/answer/2406043).

## Overriding IAM deny policies

Even if an account has the Owner or Looker Studio Pro Manager role, an [IAM deny policy](https://docs.cloud.google.com/iam/docs/deny-access) at the organization, folder, or project level might block access to Data Studio Pro features. Deny policies override allow policies. If a deny policy blocks the `lookerstudio.pro.manage` permission, you won't be able to start or manage a Pro subscription.

### Check for deny policies

If you have Organization Administrator permissions, or the Deny Reviewer (`roles/iam.denyReviewer`) or Deny Admin (`roles/iam.denyAdmin`) role, you can use [Policy Troubleshooter](https://docs.cloud.google.com/iam/docs/troubleshooting-access#policy-troubleshooter) to check whether access is denied:

  1. In the Google Cloud console, go to the **Policy Troubleshooter** page. 

[Go to Policy Troubleshooter](https://console.cloud.google.com/iam-admin/troubleshooter)

  2. For **Principal** , enter your email address.
  3. For **Resource** , enter the project ID.
  4. For **Permission** , enter `lookerstudio.pro.manage`.
  5. Click **Check Access**.



If Policy Troubleshooter indicates that access is denied, it provides details about the policy that causes the block. For instructions on updating deny policies, see [Deny access to resources](https://docs.cloud.google.com/iam/docs/deny-access).

## Related resources

  * [Start a new Pro subscription](https://docs.cloud.google.com/data-studio/start-a-new-pro-subscription)
  * [Step 1: Select a Google Cloud project](https://docs.cloud.google.com/data-studio/step-1-select-a-google-cloud-project)
  * [Step 2: Add people to the subscription](https://docs.cloud.google.com/data-studio/step-2-add-people-to-the-subscription)
  * [Edit a Pro subscription](https://docs.cloud.google.com/data-studio/edit-a-pro-subscription)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
