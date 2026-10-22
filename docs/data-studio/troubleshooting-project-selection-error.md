---
url: https://docs.cloud.google.com/data-studio/troubleshooting-project-selection-error/
title: Troubleshoot project selection error during Data Studio Pro activation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:52.073591+00:00
---

# Troubleshoot project selection error during Data Studio Pro activation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/troubleshooting-project-selection-error/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Troubleshoot project selection error during Data Studio Pro activation Stay organized with collections  Save and categorize content based on your preferences. 

When activating a Data Studio Pro subscription, you might encounter an error message that says `Project is a valid Google Cloud project and you have the permissions`. This error can occur for several reasons, including incorrect project configuration or insufficient permissions.

![](https://docs.cloud.google.com/static/data-studio/images/lsp-project-error.png)

This document describes several potential causes for this error and provides steps to troubleshoot them.

## Decision tree

Use the following decision tree to troubleshoot errors that you might encounter when activating a Data Studio Pro subscription:

## Troubleshooting steps

The following sections describe the scenarios in the tree in further detail.

## Missing IAM permissions

To activate a Data Studio Pro subscription for a Google Cloud project, you must have the correct IAM permissions on that project.

**How to troubleshoot:**

Ensure that you have one of the following Identity and Access Management roles for the project that you are associating with Data Studio Pro:

  * Owner (`roles/owner`)
  * Looker Studio Pro Manager (`roles/lookerstudio.proManager`)



These roles include the project-level permissions that are needed to activate and manage your subscription. See [Data Studio Pro roles and permissions](https://docs.cloud.google.com/data-studio/about-pro-roles-and-permissions) for more information.

## Overriding IAM deny policy

Even if you have the Owner or Looker Studio Pro Manager Identity and Access Management role, an [IAM deny policy](https://docs.cloud.google.com/iam/docs/deny-access) at the organization, folder, or project level might be blocking you from activating Data Studio Pro. Deny policies override allow policies (like those granted by IAM roles). If a deny policy exists that blocks the `lookerstudio.pro.manage` permission, you won't be able to complete the activation.

**How to troubleshoot:**

If you have Organization Administrator permissions, or if you have the Deny Reviewer (`roles/iam.denyReviewer`) or Deny Admin (`roles/iam.denyAdmin`) role, you can check for deny policies that might affect your project.

You can use the [Policy Troubleshooter](https://docs.cloud.google.com/iam/docs/troubleshooting-access#policy-troubleshooter) to check why access might be denied:

  1. In the Google Cloud console, go to the **Policy Troubleshooter** page. 

[Go to Policy Troubleshooter](https://console.cloud.google.com/iam-admin/troubleshooter)

  2. For **Principal** , enter your email address.
  3. For **Resource** , enter the project ID.
  4. For **Permission** , enter `lookerstudio.pro.manage`.
  5. Click **Check Access**.



If Policy Troubleshooter indicates that access is denied, it will provide information about the policy that is causing the denial. For more information about managing deny policies, see [Deny access to resources](https://docs.cloud.google.com/iam/docs/deny-access).

## Project not linked to an active billing account

A Data Studio Pro subscription must be linked to a Google Cloud project that has an active Cloud Billing account.

**How to troubleshoot:**

Ensure that the project that you use for Data Studio Pro is linked to an active billing account. For more information, see [Enable billing for an existing project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_an_existing_project).

## User and project are in different organizations

If you try to activate Data Studio Pro by using a Google Cloud project that belongs to a different organization than your user account, you might encounter this error.

**How to troubleshoot:**

Ensure that your user account and the Google Cloud project are in the same organization.

## Incorrect user account type

Data Studio Pro subscriptions must be associated with a Google Workspace or Cloud Identity organization. You can't sign up for Data Studio Pro with a personal Google Account (such as an @gmail.com account).

**How to troubleshoot:**

Make sure that you are signed in with your managed Google Workspace or Cloud Identity account before you try to activate Data Studio Pro.

## Project already has a Data Studio Pro subscription

Each Google Cloud project can be associated with only one Data Studio Pro subscription.

**How to troubleshoot:**

If the project that you selected is already linked to a Data Studio Pro subscription, you must select a different project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
