---
url: https://docs.cloud.google.com/migration-center/docs/postgresql-preferences/
title: Migration preferences for PostgreSQL \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:48.448422+00:00
---

# Migration preferences for PostgreSQL  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/postgresql-preferences/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Migration preferences for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the available migration preferences for PostgreSQL database deployments. As your target product, you can select AlloyDB for PostgreSQL or Cloud SQL for PostgreSQL.

## Cloud SQL for PostgreSQL settings

Migration Center lets you choose Cloud SQL as the target database deployment for your database.

  * From the **Cloud SQL edition** list, select the edition to which you want to migrate. For more information, see [Cloud SQL editions features](https://docs.cloud.google.com/sql/docs/editions-intro#edition-features).


  * From the **Sizing method** list, select the sizing strategy that you want to apply during the migration. If you select **Utilization based** , Migration Center uses performance metrics from your database, if available, to provide sizing recommendations.


  * From the **Storage type** list, select the type of storage that you want to use for your database.



### Availability

Specify how to distribute your database across Google Cloud zones.

  * From the **Zones** list, select either **Single zone** or **Multiple zones**. Choosing multiple zones for your database provides a backup zone in case the primary zone becomes unavailable.



For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

### Automatic backup

Specify if you want to enable automatic backups.

For more information, see [About Cloud SQL backup](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups).

### Pricing track

Specify your preferred pricing track for the database that you migrate to Google Cloud.

Choose between on demand pricing, or a committed use of one or three years. Committed use discounts (CUDs) apply when you choose a committed use, and appear in your total cost of ownership (TCO) report.

For more information, see [Cloud SQL pricing](https://docs.cloud.google.com/sql/docs/postgres/pricing).

## AlloyDB for PostgreSQL settings

Migration Center lets you choose AlloyDB for PostgreSQL as the target database deployment for your database. Choose the settings for your database as described in the following sections.

### Sizing

Specify your preferred sizing strategy for the database that you migrate to Google Cloud.

From the **Sizing method** list, select one of the following sizing strategies to apply in your assessment:

  * **No rightsizing:** choose a shape that closely matches the shape of your source machine. Sizing doesn't take performance data into account.
  * **Shape based:** choose a shape that is rightsized based on AlloyDB's efficient use of resources.
  * **Utilization based:** choose a shape that is rightsized based on AlloyDB's efficient use of resources, and on the source performance data, when available.



### Primary instance availability

Specify how to distribute your database across Google Cloud zones.

From the **Zones** list, select either **Single zone** or **Multiple zones**. Choosing multiple zones for your database provides a backup zone in case the primary zone becomes unavailable.

### Data protection

From the **Continuous data protection** field, specify if you plan to use automatic backups in your database, and to include them in your cost estimation.

### Pricing track

Specify your preferred pricing track for the database that you migrate to Google Cloud.

Choose between on demand pricing, or a committed use of one or three years. Committed use discounts (CUDs) apply when you choose a committed use, and appear in your TCO report.

For more information, see [AlloyDB for PostgreSQL pricing](https://cloud.google.com/alloydb/pricing).

## What's next

  * Learn about the [available preferences for MySQL databases](https://docs.cloud.google.com/migration-center/docs/mysql-preferences).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
