---
url: https://docs.cloud.google.com/data-studio/cms/
title: Use customer-managed storage \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:55.755890+00:00
---

# Use customer-managed storage  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/cms/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Use customer-managed storage Stay organized with collections  Save and categorize content based on your preferences. 

**Data Studio Pro feature**

The features and functionality described in this page are available to Data Studio Pro users.

[Get Data Studio Pro.](https://docs.cloud.google.com/data-studio/about-pro)

Customer-managed storage lets you store your Data Studio Pro data in your own Cloud Storage bucket instead of in Google-managed storage. Using customer-managed storage in Data Studio Pro gives you greater control over your data, lets you configure retention policies, and lets you use Google Cloud features like CMEK and VPC Service Controls.

When you enable customer-managed storage for your Data Studio Pro subscription, Customer Core Content is stored in the following locations:

  * Data extracts: BigQuery
  * Excel file uploads: Cloud Storage and BigQuery
  * CSV file uploads: Cloud Storage



## Before you begin

In order to enable and use customer-managed storage, you must meet the following prerequisites:

  * You can enable customer-managed storage only for a new Data Studio Pro subscription.
  * You must be an administrator in your Data Studio Pro organization.
  * You must create a Cloud Storage bucket and BigQuery dataset created in your Data Studio Pro project. If you selected a data region other than 'global' when [setting up data residency](https://docs.cloud.google.com/data-studio/data-residency), you must set up your bucket and dataset in the same data region.
  * You must grant the Data Studio Pro service account the following IAM roles: 
    * `roles/datastudio.managedStorageServiceAgent` (Data Studio Managed Storage Service Agent) on the Cloud Storage bucket
    * `roles/datastudio.managedStorageServiceAgent` (Data Studio Managed Storage Service Agent) on the BigQuery dataset
    * `roles/datastudio.serviceAgent` (Data Studio Service Agent) on your project



If you want to create a custom role to use customer-managed storage, you need the following permissions:

  * `bigquery.datasets.get`
  * `bigquery.jobs.create`
  * `bigquery.tables.create`
  * `bigquery.tables.delete`
  * `bigquery.tables.getData`
  * `bigquery.tables.list`
  * `bigquery.tables.updateData`
  * `serviceusage.services.use`
  * `storage.buckets.get`
  * `storage.objects.create`
  * `storage.objects.get`
  * `storage.objects.delete`
  * `storage.objects.list`



## Enable customer-managed storage

To enable customer-managed storage, follow these steps while creating a new Data Studio Pro subscription:

To complete the customer-managed storage setup step during subscription creation:

  1. Navigate to the **Customer-managed storage** section of the setup flow.
  2. Enter your **GCS bucket name** and **BigQuery dataset id** in the corresponding fields.
  3. Click **Next**.



As a Google Cloud administrator, you can also enforce that all new Data Studio Pro subscriptions are set up with customer-managed storage.

## Disable customer-managed storage

You can disable customer-managed storage only when you create a new subscription.

To disable customer-managed storage for an existing subscription, you must [cancel the subscription](https://docs.cloud.google.com/data-studio/cancel-a-pro-subscription).

## Limitations of customer-managed storage

Customer-managed storage has the following limitations:

  * If you downgrade from Data Studio Pro to the no-cost version of Data Studio, or if your subscription is canceled, customer-managed storage features will continue to work for a 30-day grace period. After that, data sources created using customer-managed storage will be deleted.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
