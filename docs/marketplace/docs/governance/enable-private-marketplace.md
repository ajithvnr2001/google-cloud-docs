---
url: https://docs.cloud.google.com/marketplace/docs/governance/enable-private-marketplace/
title: Turn on Private Marketplace \u00a0|\u00a0 Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:59:29.735691+00:00
---

# Turn on Private Marketplace  |  Google Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/governance/enable-private-marketplace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Guides ](https://docs.cloud.google.com/marketplace/docs/overview)



Send feedback 

#  Turn on Private Marketplace Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to turn on Google Cloud Private Marketplace for your organization's users.

Collections are curated lists of approved products. To share collections with users in your organization, you must turn on Private Marketplace.

After you turn on Private Marketplace, your organization's private marketplace is the default marketplace experience for your users. Google Cloud Private Marketplace shows all approved products to your users and restricts access to products that aren't in the collections you've shared with them. Your users can still choose to navigate to and access the public marketplace.

**Note:** When you turn Private Marketplace on or off, it might take up to five minutes for this change to take effect.

Turning on Private Marketplace affects all future deployments of Google Cloud Marketplace products in your organization, but it doesn't affect existing deployments. However, if existing deployments need to be redeployed, due to events such as autoscaling or load balancing in a cluster, those deployments might be disrupted if your users don't have access to the products that the deployments use.

## Before you begin

  * Ensure that you have the [required Identity and Access Management (IAM) roles](https://docs.cloud.google.com/marketplace/docs/governance/private-marketplace#permissions).
  * [Create and publish a default collection](https://docs.cloud.google.com/marketplace/docs/governance/create-default-collection).
  * Optionally, [create](https://docs.cloud.google.com/marketplace/docs/governance/curate-collection#create) and [share](https://docs.cloud.google.com/marketplace/docs/governance/share-collection#share) additional collections.
  * Optionally, if you've turned on [strict user access restriction](https://docs.cloud.google.com/marketplace/docs/governance/strict-user-access), ensure that all of your organization's users and administrators who use your organization's marketplace have the necessary IAM roles and permissions for strict user access restriction. For more information, see [Required IAM roles](https://docs.cloud.google.com/marketplace/docs/governance/strict-user-access#permissions).



## Turn on Private Marketplace

You can turn on Private Marketplace for an entire Google Cloud organization, or for specific folders or projects within your organization.

### Turn on Private Marketplace for all projects in your organization

To turn on Private Marketplace for all of the projects in your Google Cloud organization, complete the following steps:

  1. In the Cloud Marketplace resource selector, select your organization.

  2. In the navigation menu, click **Marketplace Governance**.

[Go to Marketplace](https://console.cloud.google.com/marketplace)

  3. In the navigation menu, click **Governance Settings**.

  4. Under _Private Marketplace_ , click **Add**.

  5. Choose the _organization_ resource hierarchy node, and then click **Select**.

  6. Click the _Enable Private Marketplace_ toggle.




### Turn on Private Marketplace for specific projects or folders

To turn on Private Marketplace for specific projects or folders within your Google Cloud organization, complete the following steps:

  1. In the Cloud Marketplace resource selector, select your organization.

  2. In the navigation menu, click **Marketplace Governance**.

[Go to Marketplace](https://console.cloud.google.com/marketplace)

  3. In the navigation menu, click **Governance Settings**.

  4. Under _Private Marketplace_ , click **Add**.

  5. Choose the project or folder that you want to turn on Private Marketplace for, and click **Select**.

  6. Optionally, repeat the previous step for relevant projects or folders in your organization.

  7. Click the **Enable Private Marketplace** toggle.


**Note:** If the Private Marketplace experience is only enabled for a subset of projects or folders in your organization, users interacting with the remaining Google Cloud projects in your organization continue to see the default public marketplace experience when they navigate to Google Cloud Marketplace.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
