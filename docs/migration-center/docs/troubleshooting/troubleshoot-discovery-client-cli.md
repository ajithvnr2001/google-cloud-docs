---
url: https://docs.cloud.google.com/migration-center/docs/troubleshooting/troubleshoot-discovery-client-cli/
title: Troubleshoot issues with Migration Center discovery client CLI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:54.590747+00:00
---

# Troubleshoot issues with Migration Center discovery client CLI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/troubleshooting/troubleshoot-discovery-client-cli/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Troubleshoot issues with Migration Center discovery client CLI Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with the Migration Center discovery client CLI.

## Upgrade issue

When you upgrade the `mcdc` CLI to the latest version, it performs an internal database schema upgrade which automatically creates a backup of collected and assessed data by the previous version.

In rare cases, the `mcdc` CLI upgrade doesn't complete successfully due to a failure in upgrading the local database. This might happen due to a malfunction during the database upgrade which corrupts the database, and therefore, the previously collected data is lost.

After upgrading the `mcdc` CLI, when you run the latest version, if you see an error which indicates that the database upgrade failed, you can use the `recover-db` command to restore the database to a previous working version then downgrade to the previous `mcdc` CLI version.

Perform the following steps:

  1. Restore the database to a previous working version:
         
         ./mcdc discover recover-db
         

  2. [Download](https://docs.cloud.google.com/migration-center/docs/download-collector-cli) the the `mcdc` CLI version you used before the upgrade.

While installing an older version the `mcdc` CLI, don't remove the `mcdc` CLI directory that is created by the current version.

**Note:** On Linux machines, the lowest version of `mcdc` CLI that you can downgrade to is version 2.0.0.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
