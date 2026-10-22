---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/backup-overview/
title: Back up and restore AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.2 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:58.498543+00:00
---

# Back up and restore AlloyDB Omni  |  AlloyDB Omni for containers: 15.5.2  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/backup-overview/

This page documents AlloyDB Omni version **15.5.2** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/overview)



Send feedback 

#  Back up and restore AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.2keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/backup-overview)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/backup-overview)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/backup-overview)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/backup-overview)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/backup-overview)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/backup-overview)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/backup-overview)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/backup-overview)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/backup-overview)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/backup-overview)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/backup-overview)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/backup-overview)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/backup-overview)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/backup-overview)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/backup-overview)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/backup-overview)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/backup-overview)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/backup-overview)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/backup-overview)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/backup-overview)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/backup-overview)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/backup-overview)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/backup-overview)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/backup-overview)

This page provides an overview of data backup and restore solutions available to AlloyDB Omni database clusters. 

Because AlloyDB Omni is PostgreSQL compatible, various backup solutions developed and supported by the PostgreSQL community are also available to AlloyDB Omni databases. In general, any solution that allows you to back up from and restore to a PostgreSQL cluster running in a Docker container will also work with AlloyDB Omni.

The way that you set up and operate backup and restore features depends on whether you operate AlloyDB Omni on individual servers using the `alloydb` command-line tool, or whether you run AlloyDB Omni using the AlloyDB Omni Operator. The following sections explore these options in further detail.

## Single-server backup solutions

If you run AlloyDB Omni in a container on individual servers, then Google recommends using either [Barman](https://pgbarman.org) or [pgBackRest](https://pgbackrest.org/), depending on your needs and preferences.

Both of these open source solutions provide the following:

  * Essential data backup and restore features, including point-in-time recovery
  * Compatibility with the containerized PostgreSQL-compatible databases that AlloyDB Omni uses



Barman has the following distinct features:

  * Backups stored in a separate backup server that you manage
  * The option for cascading backup servers
  * Near-zero-data-loss backups using streamed data changes
  * The option for zero-data-loss backups using synchronous streaming



For more information, see [Set up Barman for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install-configure-barman).

pgBackRest has the following distinct features:

  * Parallelized backup jobs
  * Full, incremental, or differential backups
  * Encrypted backups
  * Backup compression and checksums
  * The option to restore only specific databases



For more information, see [Set up pgBackRest for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/set-up-pgbackrest).

## What's next

  * [Set up Barman for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install-configure-barman)

  * [Set up pgBackRest for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/set-up-pgbackrest)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
