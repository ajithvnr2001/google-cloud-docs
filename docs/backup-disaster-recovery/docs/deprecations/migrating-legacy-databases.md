---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations/migrating-legacy-databases/
title: Migrate from legacy database backups \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:32.440946+00:00
---

# Migrate from legacy database backups  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations/migrating-legacy-databases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Resources ](https://docs.cloud.google.com/backup-disaster-recovery/docs/resources)



Send feedback 

#  Migrate from legacy database backups Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This guide applies specifically to the database deprecation announced in July 2026. For information about the broader deprecation of the appliance management console announced in September 2026, see [Deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

As of July 31, 2026, Backup and DR deprecates support for database backups created by using the appliance management console. This guide describes how to migrate your existing backups and transition to alternative backup solutions.

## Affected databases

  * [SAP ASE](https://www.sap.com/products/data-cloud/sybase-ase.html)
  * [SAP IQ](https://www.sap.com/products/data-cloud/sybase-iq-big-data-management.html)
  * [SAP MaxDB](https://maxdb.sap.com/)
  * [MariaDB](https://mariadb.com/)
  * [MySQL](https://www.mysql.com/)
  * [PostgreSQL](https://www.postgresql.org/)



## Key points and dates

Support for creating _new_ backups of the affected databases by using the appliance management console ends on July 31, 2027. You must migrate any existing backup data you want to retain from the appliance management console by December 30, 2027.

### July 31, 2027

On July 31, 2027, the ability to create _new_ backups for existing setups of the affected databases in the appliance management console ends.

### December 30, 2027

On December 30, 2027, the migration period ends. You must complete the export of any backup data that you want to retain from the appliance management console. Access to these backups through the appliance management console isn't guaranteed after this date.

## Recommended actions

To avoid losing your data, we recommend that you take the following actions:

  1. Assess your current backups and identify which instances of the affected databases are backed up by using the appliance management console.
  2. Restore any data you want to keep from backups taken with the appliance management console before December 30, 2027.



## Alternative backup solutions

The following sections describe alternative backup solutions based on your database type.

### MySQL and PostgreSQL

For MySQL and PostgreSQL databases, we recommend that you migrate your database instances to Google Cloud fully managed database services:

  * Cloud SQL
  * AlloyDB for PostgreSQL



### SAP ASE, SAP IQ, SAP MaxDB, and MariaDB

Google doesn't provide a direct first-party replacement for backing up these databases by using the appliance management console. We recommend the following alternative backup solutions.

**Note:** The solutions in this section are also applicable to self-managed MySQL and PostgreSQL databases.

  * **Native database backup utilities** : use the built-in backup and dump commands provided by the database vendor.

    * For MariaDB and MySQL, use `mysqldump`.
    * For PostgreSQL, use `pg_dump`.
    * For SAP ASE, SAP IQ, and SAP MaxDB, use SAP's backup tools.
    * Schedule backups to run regularly.
    * Store backup files securely in a [Cloud Storage bucket](https://docs.cloud.google.com/storage). Consider using appropriate storage classes based on access needs and cost.

This option provides full control over the backup process, but requires manual setup, scripting, and scheduling.

  * **Third-party backup solutions** : Explore backup and recovery solutions from Google Cloud partners on the [Google Cloud Marketplace](https://console.cloud.google.com/marketplace).

    * Partners such as Veeam and Cohesity offer backup and recovery support for these databases.

This option provides centralized management and automation, but requires additional cost and vendor management.




## Export data from existing backups

To retain data from backups taken by using the deprecated appliance management console feature, you must restore the data to a live environment. You can use the Backup and DR service to perform these restores until December 30, 2027. For instructions on how to perform restore operations, see [Recovering database data](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/recover-otherdb).

## Support and assistance

To help you plan your migration, Google Cloud provides the following resources:

  * **Account team** : reach out to your Google Cloud account team for personalized guidance and assistance in planning your migration.

  * **Email support** : for specific questions related to this transition, send an email to [gcbdr-umdb-transition@google.com](mailto:gcbdr-umdb-transition@google.com).

  * **Support extensions** : if you require additional time beyond the December 30, 2027, deadline to complete data exports, you can request a support extension. Google Cloud evaluates these requests on a case-by-case basis. To initiate a request, contact Cloud Customer Care or send an email to [gcbdr-umdb-transition@google.com](mailto:gcbdr-umdb-transition@google.com).




Start planning your migration as soon as possible to ensure a smooth transition.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
