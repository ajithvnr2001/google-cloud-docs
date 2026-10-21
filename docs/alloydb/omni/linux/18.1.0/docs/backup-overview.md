---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/backup-overview/
title: Back up and restore AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using RPM: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:41.988759+00:00
---

# Back up and restore AlloyDB Omni  |  AlloyDB Omni using RPM: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/backup-overview/

This page documents AlloyDB Omni version **18.1.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/overview)



Send feedback 

#  Back up and restore AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/backup-overview)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/backup-overview)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/backup-overview)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/backup-overview)

This page provides an overview of data backup and restore solutions available to AlloyDB Omni database clusters. 

Because AlloyDB Omni is PostgreSQL compatible, various backup solutions developed and supported by the PostgreSQL community are also available to AlloyDB Omni databases. Any solution that lets you back up from and restore to a PostgreSQL cluster running in a Docker or Podman container also works with AlloyDB Omni.

## Single-server backup solutions

If you run AlloyDB Omni as a systemd service on individual servers, we recommend you use [pgBackRest](https://pgbackrest.org/). pgBackRest performs physical database cluster backups.

pgBackRest has the following features:

  * Perform full, incremental, or differential backups
  * Write to local disk, remote disk, or Cloud Storage destinations
  * Parallelize and encrypt backups
  * Compression and checksums (done in-stream) options
  * Automatic management and expiration of backups



The RPM package lets you perform the following tasks:

  * Perform physical backups and restorations of your database clusters.
  * Build clone clusters, either to a current or to a specific point in time.
  * Perform selective restores of specific databases from within your database cluster.



For more information, see [Set up pgBackRest for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/set-up-pgbackrest).

Backups are transparent for TDE-enabled clusters, and you don't need to perform any additional steps to take a backup. For more information, see [Create a TDE-enabled cluster](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/create-tde-cluster).

## What's next

  * [Set up pgBackRest for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/set-up-pgbackrest)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
