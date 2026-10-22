---
url: https://docs.cloud.google.com/architecture/identity/overview-assess-and-plan/
title: Plan the onboarding process for your corporate identities \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:06.188357+00:00
---

# Plan the onboarding process for your corporate identities  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/overview-assess-and-plan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Plan the onboarding process for your corporate identities Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-06-26 UTC

The documents in the **Assess and plan** section help you assess your requirements and develop a plan for onboarding your corporate identities to Cloud Identity or Google Workspace.

Managing corporate identities is often one of the key responsibilities of enterprise IT departments. But each organization is unique, and the way you manage corporate identities in your organization is likely to be unique, too. To determine the best way to use [Cloud Identity](https://docs.cloud.google.com/identity) or [Google Workspace](https://gsuite.google.com/) to manage corporate identities in your organization, it's important that you assess your requirements.

## Before you begin

Before you begin to assess and plan your Cloud Identity or Google Workspace deployment, make sure that you do the following:

  * Understand the [domain model](https://docs.cloud.google.com/architecture/identity/overview-google-authentication) that underpins Cloud Identity and Google Workspace.
  * Determine whether you need a single Google Cloud organization or multiple Google Cloud organizations for your deployment. For help with this decision, see [Best practices for planning accounts and organizations](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning).
  * Review the [Reference architectures](https://docs.cloud.google.com/architecture/identity/reference-architectures) article and select the architecture that most closely matches your requirements.
  * If you selected an architecture that [uses an external identity provider (IdP)](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp), review [Best practices for federating Google Cloud with an external identity provider](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating) so that you can incorporate these best practices in your design.



## Assess and planning your deployment

To assess and plan your Cloud Identity or Google Workspace deployment, follow these steps:

  1. If you selected an architecture that uses an external IdP, learn how to map the logical model of your external IdP to Cloud Identity or Google Workspace.

If you use Active Directory, refer to [Federating with Active Directory](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction) to learn how to map forests, domains, users, and groups and learn which configuration options to consider.

Similarly, if you plan to federate with Azure Active Directory (AD), see [Federate Google Cloud with Microsoft Entra ID](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory) for more details on how you can map tenants, domains, users, and groups.

  2. Identify and assess existing user accounts. If you haven't been using Google Workspace or Cloud Identity, it's possible that your organization's employees have been using consumer accounts to access Google services. Before you set up Google Workspace or Cloud Identity, we recommend that you analyze user accounts that exist and how to best deal with them.

For more details on the different sets of user accounts you might have and how they can impact your deployment, see [Assess existing user accounts](https://docs.cloud.google.com/architecture/identity/assessing-existing-user-accounts).

  3. Settle on a high-level plan for onboarding identities to Cloud Identity or Google Workspace. In [Assess onboarding plans](https://docs.cloud.google.com/architecture/identity/assessing-onboarding-plans), you can find a selection of proven onboarding plans, along with guidance on how to select the plan that best suits your needs.

If you plan to use an external IdP and have identified user accounts that need to be migrated, you might need to consider additional requirements when configuring your external IdP. For more details, see [Assess user account consolidation impact on federation](https://docs.cloud.google.com/architecture/identity/assessing-consolidation-impact-on-federation).




When you have completed your assessment and created a plan, you will be ready to onboard your corporate identities to Cloud Identity or Google Workspace.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-06-26 UTC."],[],[]] 
