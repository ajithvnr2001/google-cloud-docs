---
url: https://docs.cloud.google.com/compute/docs/instances/mysql/discover-mysql/
title: MySQL on Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:55:44.629485+00:00
---

# MySQL on Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/mysql/discover-mysql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  MySQL on Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

MySQL is one of the most popular open source relational databases, offering robust transaction processing at low costs. For a general overview of MySQL, see [What is MySQL](https://cloud.google.com/mysql).

There are several ways that you can deploy MySQL as part of your Google Cloud project:

  * _Cloud SQL_ offers MySQL as a web service. You can use Cloud SQL to host your MySQL database in Google's cloud, and let Google Cloud handle administrative duties like replication, patch management, and database management. For an overview, see [Cloud SQL overview](https://docs.cloud.google.com/sql/docs/introduction).
  * _Google Cloud Marketplace_ lets you click to install MySQL onto a Compute Engine instance. To browse available MySQL installation options from Cloud Marketplace in the Google Cloud console:

[Go to Cloud Marketplace](https://console.cloud.google.com/marketplace/browse?q=mysql)

  * You can _manually install and customize_ MySQL on Compute Engine. For manual installation instructions, see [Install MySQL on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/mysql/setup-mysql). To optimize your configuration of MySQL, follow the guide at [Configure MySQL on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/mysql/mysql-workloads).




## Choose the best MySQL deployment option for your needs

To understand which MySQL deployment option best fits your needs, consider the options as follows:

### Try Cloud SQL (recommended)

If you want the convenience of having Google Cloud take care of the backend database and server administration chores, we recommend that you use [Cloud SQL](https://docs.cloud.google.com/sql/docs/introduction). Cloud SQL provides the following advantages:

  * Automated backups
  * Point-in-time recovery
  * Replication of your data across multiple [zones](https://docs.cloud.google.com/docs/geography-and-regions) for greater availability and resiliency.



If you require MySQL features that Cloud SQL doesn't support, such as user defined functions or the SUPER privilege, you can explore the options that follow. For more information about the features that Cloud SQL supports, see the [Cloud SQL FAQ](https://docs.cloud.google.com/sql/faq#supportmysqlfeatures).

### Explore Google Cloud Marketplace deployment options

Cloud Marketplace offers several options for MySQL installations, including:

  * A standalone MySQL installation
  * LAMP stacks
  * LEMP stacks
  * Nginx stacks
  * A Percona MySQL Cluster installation



Browse available MySQL installation options from Cloud Marketplace in the Google Cloud console:

[Go to Google Cloud Marketplace](https://console.cloud.google.com/marketplace/browse?q=mysql)

### Manually install MySQL

If the previous options don't fit your requirements, such as if you want to deploy MySQL on a custom image you created, or if you want complete control of the installation process, you can manually install MySQL by creating a Compute Engine instance and installing MySQL directly onto it. For more detailed instructions, see [Install MySQL on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/mysql/setup-mysql).

## What's next

  * For best practices and tips for running MySQL workloads on Compute Engine, see [Configure MySQL on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/mysql/mysql-workloads).
  * For more information about Cloud SQL, see the [Cloud SQL for MySQL documentation](https://docs.cloud.google.com/sql/docs/mysql).
  * Browse the MySQL installation options from Cloud Marketplace in the Google Cloud console:

[Go to Cloud Marketplace](https://console.cloud.google.com/marketplace/browse?q=mysql)

  * To manually install MySQL on a Compute Engine instance, see [Install MySQL on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/mysql/setup-mysql).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
