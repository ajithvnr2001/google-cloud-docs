---
url: https://docs.cloud.google.com/looker/docs/best-practices/flows/pdt-troubleshooting/
title: Troubleshooting PDTs \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:38.624973+00:00
---

# Troubleshooting PDTs  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/flows/pdt-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Troubleshooting PDTs Stay organized with collections  Save and categorize content based on your preferences. 

This guide helps you troubleshoot PDTs on your Looker instance. To get started, go to the section that best describes your issue:

  * PDTs are failing to build
  * PDTs are building too frequently



## PDTs are failing to build

If one or more PDTs are failing to build, check the steps in this section. (If, instead, PDTs are building too frequently, check the PDTs are building too frequently section.)

Use the following decision tree to begin troubleshooting PDTs that are failing to build:

### Manually rebuild the PDT

First, test if you can successfully build or rebuild the PDT manually. If this attempt fails, [check the build failure error message](https://docs.cloud.google.com/looker/docs/admin-panel-database-pdts) for more information.

If you can successfully build your PDTs manually, then check the persistence strategy.

### Check connection settings

If all PDTs across a single connection are failing to build, check your connection settings. Insufficient scratch schema privileges are a common reason for build failures. Double-check that the [scratch schema has been set up correctly](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_tables). If the scratch schema has been changed recently, first try updating the **Connection** settings.

If you can successfully build your PDTs manually, and your connection settings are set up correctly, then there is likely an [issue with the PDT regenerator](https://docs.cloud.google.com/looker/docs/derived-tables#the_looker_regenerator) on your instance. Reach out to Support to troubleshoot this edge case.

## PDTs are building too frequently

If one or more PDTs are building too frequently, follow the steps in this section.

Use the following decision tree to begin troubleshooting PDTs that are building too frequently:

### Too many PDTs in scratch schema

Configuring multiple active Looker instances (such as a production instance and a secondary UAT or staging instance) to share the same database connection and scratch schema can cause several issues. Because each Looker instance runs its own independent garbage collector (reaper) process, sharing a scratch schema can cause the following errors:

  * Each instance's reaper operates independently. The secondary instance's reaper will identify the primary instance's PDTs as unregistered or orphaned and delete them.
  * This deletion causes the primary instance to report `Not Found` errors (such as BigQuery `Not found: Table`/404 errors) when attempting to query its own PDTs, or list `table not in scratch schema` as the build reason.
  * Both instances will continually trigger rebuilds, causing background PDT processes to churn constantly, creating race conditions, and leading to severe query volume spikes on the underlying data warehouse.



To resolve or prevent this interference, do the following:

  * Configure a unique database connection definition and a different scratch schema (or temporary dataset/database) for each active Looker instance.
  * If you must share connection settings for testing on a secondary instance, completely disable PDTs for all connections on that secondary instance, and disable all developer schedules, datagroups, and alerts to prevent background activity.



### Check the build reason in the PDT Activity dashboard

Check the [PDT Activity dashboard](https://docs.cloud.google.com/looker/docs/admin-panel-database-pdts#pdt_activity_dashboard) for more information. In particular, check the **Build reason** for the PDT that is building too frequently. Some common build reasons include the following:

  * **The table isn't in the scratch schema** : The PDT was built because no version of this PDT was found in the scratch schema. Try checking your connection settings and changing your scratch schema. If you have multiple Looker instances, such as a production instance and a QA instance, make sure to set different scratch schemas for each instance to avoid PDT management conflicts.
  * **Manual rebuild** : The PDT was manually rebuilt by a user. Check for the user's ID and see if that user is manually triggering too many PDT builds.
  * **Dependent PDT builds** : This PDT was built because another PDT depends on it. Find the dependent PDT and check its persistence strategy.



## Final review and support

If you're still having trouble with your PDTs, review the troubleshooting steps on this page. If you're still unable to resolve the issue, [contact Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
