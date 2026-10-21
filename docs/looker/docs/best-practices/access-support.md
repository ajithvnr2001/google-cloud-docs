---
url: https://docs.cloud.google.com/looker/docs/best-practices/access-support/
title: Why can't I access in-app support (chat support) for Looker (original)? \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:38.793534+00:00
---

# Why can't I access in-app support (chat support) for Looker (original)?  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/access-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Why can't I access in-app support (chat support) for Looker (original)? Stay organized with collections  Save and categorize content based on your preferences. 

This document walks you through some troubleshooting steps to determine why you cannot access in-app support (chat support) from inside the Looker (original) product. Note that in-app support isn't available for Looker (Google Cloud core) customers.

In-app support refers specifically to chat support. To create and manage general support cases, you must use the [Google Cloud console](https://console.cloud.google.com/support/cases).

## Requirements

To access in-app support (chat support), your Looker instance must meet the following requirements:

  1. Active Google Cloud Support Plan
  2. Looker Google Cloud Project
  3. Tech Support Editor IAM Role
  4. Officially Supported Looker Version



### 1\. Active Google Cloud Support Plan

Your Looker project must have an active Google Cloud Support Plan. This can be either one of our [paid support offerings](https://docs.cloud.google.com/support) or our [free Comprehensive Support](https://docs.cloud.google.com/support/docs/integrations#comprehensive_support) (exclusive to our SaaS customers).

### 2\. Looker Google Cloud Project

Your organization must have a [Looker Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). Link your [Looker Google Cloud project number](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#google_cloud_project_number) to your Google Cloud Support account in the console.

For Looker (original) instances, fill in the Looker Google Cloud project number on the [General Settings](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#google_cloud_project_number) Admin page.

You must be a Looker admin to access the General Settings Admin page.

### 3\. Tech Support Editor IAM Role

To access in-app support (chat support), you must have the Tech Support Editor IAM role.

You must be an IAM admin on your Looker project to update IAM roles and grant support access.

### 4\. Officially Supported Looker Version

Your Looker instance must be running an [officially supported Looker version](https://docs.cloud.google.com/looker/docs/officially-supported-releases).

If your organization does not have a paid support offering, complete the previous steps and email our Google Cloud Support Onboarding Team at saas-support-onboarding@google.com with your ORG ID from your Google Cloud Console. From there, we can provision our free Comprehensive Support (exclusive for SaaS customers) for Looker. If you are unsure whether your organization has an active Google Cloud Support Plan or have any issues completing the previous requirements, reach out to our Google Cloud Support Onboarding Team for further assistance. 

## Troubleshooting in-app support at the instance level

If no users can access support, the problem is likely at the instance level.

If you own a Looker license that isn't Looker (original), such as Looker (Google Cloud core), in-app chat isn't available. Instead, submit your new support requests using the [Google Cloud console](https://console.cloud.google.com/support/cases).

If you have a Looker (original) license, complete the following steps.

  1. If you don't already have a Looker project on Google Cloud, [create a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) and name it `Looker`.
  2. Go to the [Google Cloud console](https://console.cloud.google.com/) home page, select the Looker project, and copy the Looker project number.
  3. Enter your [Google Cloud project number](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#google_cloud_project_number) on the [General Settings](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#google_cloud_project_number) Admin page. The project number connects your Looker instance to your Google Cloud support plan and determines your level of support. Repeat this step for each of your Looker instances (except trials).

You must be a Looker admin to access the General Settings Admin page.



### Troubleshooting in-app support for customer-hosted instances

If your Looker instance is customer-hosted, [update your Looker instance](https://docs.cloud.google.com/looker/docs/updating-looker-instance) to a [supported Looker version](https://docs.cloud.google.com/looker/docs/officially-supported-releases).

The Looker **Help** menu displays the **Get Support** option only if the Looker instance is running a supported version.

## Troubleshooting in-app support at the user level

If support is available for some users and not other users, the problem is probably with the permissions of the users who cannot access support.

Support is available only to users with the **Tech Support Editor** [Identity and Access Management role](https://docs.cloud.google.com/iam/docs/grant-role-console). Contact your organization administrator to have the Identity and Access Management role granted under your Looker project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
