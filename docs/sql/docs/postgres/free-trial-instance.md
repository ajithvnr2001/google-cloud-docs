---
url: https://docs.cloud.google.com/sql/docs/postgres/free-trial-instance/
title: Try out Cloud SQL for PostgreSQL using a free trial instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:35.950141+00:00
---

# Try out Cloud SQL for PostgreSQL using a free trial instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/free-trial-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Try out Cloud SQL for PostgreSQL using a free trial instance Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/free-trial-instance "View this page for the MySQL database engine") | PostgreSQL | SQL Server

A Cloud SQL free trial instance lets you test the majority of Cloud SQL features for up to 30 days without any financial commitment.

## Eligibility

Both existing and new Google Cloud customers are eligible for the free trial instance, but you must create your free trial instance in a new Google Cloud project. One free trial instance is allowed per project.

To create a free trial instance, you must also enable billing:

  * **Existing user** : Ensure that you [verify billing is enabled](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#console) for your project.
  * **New user** : Sign in to the Google Cloud console with your Google Account and [set up a billing account](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#console) with your credit card or other payment method.



If you're a new Google Cloud customer, you might also be eligible for the [Google Cloud 90-day, $300 free trial](https://docs.cloud.google.com/free/docs/free-cloud-features#free-trial). The Cloud SQL free trial instance is in addition to the $300 free trial credits offered by the Google Cloud free trial.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




## Create a free trial instance

To create a free trial instance, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Get Started** page.

[Go to Cloud SQL Get Started](https://console.cloud.google.com/sql/get-started)

  2. In the **Experience Cloud SQL at no cost for 30 days** section, complete the following:

     * In the **Database Engine** field, select the database engine for your free trial instance.
     * In the **Instance ID** field, enter a name for your instance. The instance ID must start with a letter, and only use lowercase letters, numbers, and hyphens.
     * In the **Password** field, enter a password you'd like. This password is used to connect to the default database.
     * In the **Region** field, select your instance's region.
  3. Click **Create free instance**.

After you create the free trial instance, you are redirected to the **Overview** page. You can view your instance configurations, edit your instance, and the days left in your trial on this page.




### Free trial instance configuration

The free trial instance comes with the following configurations:

  * Cloud SQL Enterprise Plus edition instance
  * [N2 machine series](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview) with 8 vCPUs and 64 GB memory
  * 100 GB storage
  * 375 GB [data cache](https://docs.cloud.google.com/sql/docs/postgres/data-cache)


  * (Optional) High availability standby



## Monitor a free trial instance

You can monitor your free trial instance using the following:

  * [Monitoring dashboard](https://docs.cloud.google.com/sql/docs/postgres/monitor-instance)
  * [System insights](https://docs.cloud.google.com/sql/docs/postgres/use-system-insights)
  * [Query insights](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights)



## Check free trial instance time

To check your free trial instance's remaining time, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click your free trial instance name.
  3. In the **Overview** page, your trial's remaining time is shown at the top of the page.



## Upgrade a free trial instance

You can upgrade your free trial instance anytime during the 30-day trial period or the 90-day grace period.

To upgrade your free trial instance, complete the following steps:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click your free trial instance name.
  3. In the **Overview** page, click **Upgrade now** in the **Days left on trial** banner.
  4. In the **Upgrade your Cloud SQL free instance** page, click **Upgrade now**.



After you upgrade your instance to a paid instance, you get the following benefits:

  * Instant switch to a paid instance without loss of data or downtime.
  * Scale compute capacity by upgrading your machine size or machine series.
  * Ability to add read replicas.
  * Option to create backups and restore your backups.
  * Ability to create cross-region replica setups.
  * Ability to switch between Cloud SQL editions.



After the upgrade completes, the **Overview** page no longer shows the days left on trial information, and any limitations that apply to the free trial instance are removed. You can change your instance machine size and other settings after the upgrade is complete.

## Delete a free trial instance

To delete your free trial instance, complete the following steps:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click your free trial instance name.
  3. In the **Instance overview** page, click **Delete**.
  4. In the **Delete instance** window, complete the following:

     1. In the text field, confirm that you want to delete your free trial instance by typing your instance ID in the **Instance ID** field.
     2. If you want to create a [final backup](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#final-backup) of the instance, select the **Create a final backup** checkbox. Expand the **Retention options** menu, and then enter the number of days to retain the final backup in the **Retain for** field. The default value is 30 days, but you can specify from 1 to 365 days. You are charged for creating and storing the final backup.
     3. In the **Describe this backup** field, you can optionally provide a description of the backup.
     4. Click **Delete**.

**Note:** Once you delete your instance, you can't restart your free trial. The only way to recover your instance is to upgrade your free trial instance.

Your free trial instance is scheduled for deletion.




## Limitations and conditions

The following limitations and conditions apply to a free trial instance:

  * **Instance quota** : You are allowed only one free trial instance per project.
  * **Service level agreement (SLA) guarantee** : SLAs do not apply to free trial instances. These instances are designed for testing and learning, and they are not recommended for production applications.
  * **Duration** : The trial lasts for 30 days. You can upgrade to a paid instance at any time during this period.
  * **Expiry and grace period** : If you do not upgrade your instance before the 30-day trial period ends, the instance stops serving requests. The instance and its data are maintained at no cost during an additional 90-day grace period, after which the instance is scheduled for deletion.
  * **Explicit deletion** : If you delete your instance before either the 30-day trial period or the 90-day grace period ends, then the instance and its data are deleted immediately. No backups are created.
  * **Configuration** : The free trial instance comes with preset configurations, which you cannot modify. To increase storage or compute capacity, you must upgrade to a paid instance. For more information, see Free trial instance configuration.
  * **Backups** : Free trial instances do not support backups or restoration, except for the final backup that you can create when you delete your instance.
  * **Charges** : You aren't charged for the free trial instance and its instance resources. However, you are charged for data transfer costs for connections outside the region, connections through the public internet, and for the creation and storage of your final backup.
  * **Policy changes** : Inclusions and conditions can be changed, suspended, or discontinued at any time without prior notice.



## What's next

  * [Create and query a database](https://docs.cloud.google.com/sql/docs/postgres/create-query-database) in your free trial instance.
  * Learn more about [monitoring your instance](https://docs.cloud.google.com/sql/docs/postgres/monitor-instance).
  * Understand [Cloud SQL quotas and limits](https://docs.cloud.google.com/sql/docs/postgres/quotas).
  * Learn more about [Cloud SQL pricing](https://cloud.google.com/sql/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
