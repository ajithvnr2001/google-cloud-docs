---
url: https://docs.cloud.google.com/docs/enterprise/manage-foundation/
title: Extend your initial setup and build your architecture \u00a0|\u00a0 Get started \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:42:40.847091+00:00
---

# Extend your initial setup and build your architecture  |  Get started  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/enterprise/manage-foundation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Get started ](https://docs.cloud.google.com/docs/get-started)
  * [ Guides ](https://docs.cloud.google.com/docs/overview)



Send feedback 

#  Extend your initial setup and build your architecture Stay organized with collections  Save and categorize content based on your preferences. 

After you complete [Google Cloud Setup](https://docs.cloud.google.com/docs/enterprise/cloud-setup), you can extend your initial configuration and build your architecture.

## Extend your initial setup

Google Cloud Setup helps you create and deploy an initial configuration. To further customize your configuration to meet your organization's unique needs, you can perform the following optional procedures at any time after you complete your initial setup.

### Manage users and groups

To manage users and groups beyond the initial administrators you created, do the following:

  * To manually create additional users and groups, see the following.

    * [Create a group in your organization](https://support.google.com/cloudidentity/answer/33343).
    * [Add or invite users to a group](https://support.google.com/cloudidentity/answer/6191469).
  * If you use an identity provider such as Active Directory, Azure AD, Okta, or Ping Identity, you can federate your provider into Google Cloud. For details see the following:

    * [Reference architectures: using an external IdP](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp).
    * To automatically provision users and enable single sign-on, see [Federate Cloud Identity with Active Directory](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction).
    * To sync Active Directory users and groups to Google Cloud, see [Directory Sync](https://support.google.com/a/topic/10343447).
  * To automate identity administration tasks, see [Google Workspace Admin SDK](https://developers.google.com/admin-sdk/).




### Monitor your billing account

To monitor costs after you set up your Cloud Billing account, we recommend that you implement the following for each account:

  * For an overview of cost management best practices, see [Cost optimization](https://docs.cloud.google.com/architecture/framework/cost-optimization).
  * Export detailed Cloud Billing data (such as usage, cost estimates, and pricing data) automatically throughout the day. For more information, see [Export Cloud Billing data exports to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery).
  * Define budgets to generate alerts when spending reaches thresholds. For more information, see [Create, edit, or delete budgets and budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets).



### Customize your network

After you deploy your configuration, you can customize your initial network settings by doing the following:

  * To create and connect service projects, see [Attach service projects](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#create-shared).

  * If you create GKE instances in your projects, configure secondary [IP address ranges for VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#cluster_sizing).




### Maintain and analyze logs

After you create your initial logging configuration, do the following:

  * To query, view, and analyze logs, see [Query and view logs overview](https://docs.cloud.google.com/logging/docs/log-analytics).

  * Cloud Logging includes a free monthly allotment. You might incur additional costs as your resource use increases. For more information, see [Cloud Logging pricing summary](https://cloud.google.com/stackdriver/pricing#logging-pricing-summary).




### Give users access to support

To configure user access to support services, see [Access control with IAM](https://docs.cloud.google.com/support/docs/access-control).

## Build your Google Cloud architecture

When you are ready to experiment and build your Google Cloud architecture, see the following:

  * To quickly deploy and learn from prebuilt solutions, see [Jump Start Solution guides](https://docs.cloud.google.com/architecture/all-jss-guides).

  * To migrate your data and applications from other clouds and on-premises to Google Cloud, see [What is Google Cloud Migration Center?](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)

  * For workload migration best practices, see [Migrate to Google Cloud](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
