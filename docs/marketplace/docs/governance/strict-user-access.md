---
url: https://docs.cloud.google.com/marketplace/docs/governance/strict-user-access/
title: Manage user access with Marketplace User Access Restrictions \u00a0|\u00a0 Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:14.019731+00:00
---

# Manage user access with Marketplace User Access Restrictions  |  Google Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/governance/strict-user-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Guides ](https://docs.cloud.google.com/marketplace/docs/overview)



Send feedback 

#  Manage user access with Marketplace User Access Restrictions Stay organized with collections  Save and categorize content based on your preferences. 

By default, any user with the Identity and Access Management (IAM) permission `resourcemanager.projects.get` for a Google Cloud project can access Google Cloud Marketplace to discover new products. If you want to enforce stricter governance and procurement policies in your Google Cloud organization, you can use Marketplace User Access Restrictions to require that users have additional IAM permissions to accomplish some tasks.

## Required IAM permissions

After you turn on Marketplace User Access Restrictions, your organization's users must have the following IAM permissions to complete the following tasks:

**Action** | **IAM Roles** | **Level at which role is assigned**  
---|---|---  
Enable Marketplace User Access Restrictions | Organization Administrator (`roles/resourcemanager.organizationAdmin`) AND Commerce Organization Governance Admin (`roles/commerceorggovernance.admin`) roles | Organization level  
Interacting with products listed on the Google Cloud Marketplace | Governed Marketplace User (`roles/commerceorggovernance.user`) role | Organization, Folder, or Project level  
  
The [Governed Marketplace User](https://docs.cloud.google.com/marketplace/docs/access-control#commerceorggovernance.user) IAM role contains the following IAM permissions:

  * `commerceorggovernance.services.get`
  * `commerceorggovernance.services.list`
  * `commerceorggovernance.services.request`
  * `resourcemanager.projects.get`
  * `consumerprocurement.entitlements.list`



When Cloud Marketplace User Access Restrictions is turned on for your organization, you must have these IAM permissions to do the following:

  * `commerceorggovernance.services.list` lets you view and interact with the Google Cloud Private Marketplace homepage.
  * `commerceorggovernance.services.get` lets you interact with product listing pages.
  * If [Request Product](https://docs.cloud.google.com/marketplace/docs/governance/product-requests) is turned on, `commerceorggovernance.services.request` and `consumerprocurement.entitlements.list` let you request unapproved products or products that haven't been procured.

**Caution:** Ensure that key billing, organization, and project administrators have these roles assigned to them to not disrupt their associated Cloud Marketplace experience.

## Before you begin

  1. Ensure you have sufficient roles to enable Marketplace User Access Restrictions. You can find the required details listed above.

  2. Ensure users and administrators in your organization that require access to the Marketplace are given sufficient roles. You can find the required roles listed above.

  3. Verify that Google Cloud Private Marketplace supports the products that you plan to use. For a list of supported products, see [Supported products](https://docs.cloud.google.com/marketplace/docs/governance/private-marketplace#supported-products).




## Turn on Marketplace User Access Restrictions

By default, Marketplace User Access Restrictions is turned off for your organization.

After you've assigned the above IAM roles to relevant users and administrators in your organization, to turn this feature on, complete the following steps:

  1. In Cloud Marketplace, click **Marketplace Governance**.

[Go to Marketplace](https://console.cloud.google.com/marketplace)

  2. In Governance settings, click the toggle to enable Marketplace User Access Restrictions.

  3. Click Confirm in the dialog.


**Note:** to disable this feature, click the toggle to turn-off enforcement. The experience for all users in your organization will revert to the default Google Cloud Marketplace experience

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
