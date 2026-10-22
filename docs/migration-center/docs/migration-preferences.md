---
url: https://docs.cloud.google.com/migration-center/docs/migration-preferences/
title: Create and manage migration preferences \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:40.044192+00:00
---

# Create and manage migration preferences  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/migration-preferences/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Create and manage migration preferences Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use preferences to customize your migration plan according to your business needs.

## Migration preferences overview

Migration preferences are sets of parameters that you can define and apply to asset groups to evaluate different cloud configurations and associated costs in a [total cost of ownership (TCO) report](https://docs.cloud.google.com/migration-center/docs/generate-tco-report). Migration Center lets you create different sets of preferences that you can use to generate multiple TCO reports with different scenarios. For example, you can compare the TCO reports of running your infrastructure in different regions, or using different virtual machine (VM) types.

Migration Center lets you configure migration preferences for different asset types, including servers and database deployments. The preferences you set for servers aren't applied to databases, and the preferences you set for a specific database type don't apply to other databases or servers. When you don't set your preference, Migration Center uses default values when it generates the TCO report.

When you [activate Migration Center](https://docs.cloud.google.com/migration-center/docs/get-started-with-migration-center#activate-migration-center), a default set of preferences is created.

## Create migration preferences

You can create multiple sets of preferences to compare different migration strategies in your TCO reports.

To create a new set of preferences, follow these steps:

  1. Go to the **Migration preferences** page.

[Go to Migration preferences](https://console.cloud.google.com/migration/preferences)

  2. Click **Create migration preferences**.

  3. On the **Create migration preferences** page, fill in the sections with your preferences.

  4. To create a new set of preferences, click **Create**.




To copy and edit an existing set of preferences, click the more_vert**Actions** button next to a preference set in the **Migration preferences** page, or click the relevant action in the action bar of the migration preferences details page.

## Edit your migration preferences

To edit your preferences, follow these steps:

  1. Go the **Migration preferences** page.

[Go to Migration preferences](https://console.cloud.google.com/migration/preferences)

  2. From the list of preferences, click the preference set that you want to edit.

  3. On the **Migration preferences** page, click **Edit**.

  4. Make the changes to your preferences, then click **Save**.




## Available migration preferences

The following sections describe the preferences that you can change in Migration Center.

### Name and description

Specify a name and, optionally, provide a description for every preference set. Name and descriptions help you identify different sets of preferences and their purpose.

For the default set of preferences, you cannot edit the name and the description.

### Location

Specify the Google Cloud region where you want to run the virtual machine (VM) instances that you plan to migrate to Google Cloud.

Learn more about [Google Cloud regions](https://docs.cloud.google.com/docs/geography-and-regions).

### Server

If you plan to migrate servers or virtual machine (VM) instances to Google Cloud, specify your migration preferences.

For the full list of available preferences, see [Migration preferences for servers](https://docs.cloud.google.com/migration-center/docs/server-preferences).

### Microsoft SQL Server

If you plan to migrate a Microsoft SQL Server deployment to Google Cloud, specify your migration preferences.

For the full list of available preferences, see [Migration preferences for Microsoft SQL Server](https://docs.cloud.google.com/migration-center/docs/ms-sql-server-preferences).

### MySQL

If you plan to migrate a MySQL database deployment to Google Cloud, specify your migration preferences.

For the full list of available preferences, see [Migration preferences for MySQL](https://docs.cloud.google.com/migration-center/docs/mysql-preferences).

### PostgreSQL

If you plan to migrate a PostgreSQL database deployment to Google Cloud, specify your migration preferences.

For the full list of available preferences, see [Migration preferences for PostgreSQL](https://docs.cloud.google.com/migration-center/docs/postgresql-preferences).

## What's next

  * Learn about the [available preferences for servers](https://docs.cloud.google.com/migration-center/docs/server-preferences).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
