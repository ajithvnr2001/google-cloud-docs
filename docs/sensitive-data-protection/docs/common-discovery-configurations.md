---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/common-discovery-configurations/
title: Common discovery enablement scenarios \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:37.772315+00:00
---

# Common discovery enablement scenarios  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/common-discovery-configurations/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Common discovery enablement scenarios Stay organized with collections  Save and categorize content based on your preferences. 

This page provides high-level instructions on how to set up your discovery scan configuration for common organization-level enablement scenarios.

For information about how to create or edit a scan configuration, see [Manage scan configurations](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations).

For information about how to allow Sensitive Data Protection to discover data within a VPC Service Controls perimeter, see [Allow sensitive data discovery within service perimeters](https://docs.cloud.google.com/sensitive-data-protection/docs/allow-discovery-vpcsc).

## Profile data in an entire organization except for select projects

You can turn on discovery for an entire organization, excluding certain projects. This is useful, for example, if you want to use your [organization-level discovery subscription](https://docs.cloud.google.com/sensitive-data-protection/pricing#discovery-subscription-mode-pricing) for most—but not all—projects.

**Note:** An excluded project can still be profiled through a scan configuration with a different scope, like a project-level scan configuration.

  1. Create a scan configuration at the organization level.
  2. In the scan configuration, add a schedule and specify filters that match only the projects that you don't want to profile.
  3. In the **Frequency** tab, turn off **Do profile this data**.
  4. Click **Done**.
  5. Optional: You can add more schedules to specify how certain subsets of your organization data should be profiled. Any data that isn't specified in a schedule is profiled according to the **Catch-all schedule**.
  6. Optional: If needed, edit the catch-all schedule.
  7. Complete the rest of the scan configuration steps.



## Profile select projects or data assets in an organization or folder

In this task, you create an organization-level discovery configuration that includes only select projects or data assets.

This task is especially useful if you have an organization-level discovery subscription—such as one provided through Security Command Center—and you want to profile only one project. Project-level discovery configurations aren't included in your organization-level subscription and are billed separately. This task lets you profile the project by using an organization-level configuration so that the operation falls under your existing subscription.

To profile only a few projects or data assets across an organization or folder, follow these steps:

  1. Create a scan configuration at the organization or folder level.
  2. In the scan configuration, add a schedule and specify filters that match only the projects or assets that you want to profile.
  3. Specify the frequency and conditions for profiling the data that you selected.
  4. Click **Done**.
  5. Specify that all other data in the organization or folder shouldn't be profiled: 
     1. Go to **Catch-all schedule** , which is the last schedule in the **Schedules** list.
     2. Turn off **Profile the resources that don't match any custom schedule**.
  6. Complete the rest of the scan configuration steps. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
