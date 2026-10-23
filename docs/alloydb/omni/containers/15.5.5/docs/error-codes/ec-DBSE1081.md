---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/error-codes/ec-DBSE1081/
title: DBSE1081. Failed to promote standby database \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:54:24.535141+00:00
---

# DBSE1081. Failed to promote standby database  |  AlloyDB Omni for containers: 15.5.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/error-codes/ec-DBSE1081/

This page documents AlloyDB Omni version **15.5.5** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/overview)



Send feedback 

#  DBSE1081. Failed to promote standby database Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.5keyboard_arrow_down

  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/error-codes/ec-DBSE1081)

This error can occur during a failover or switchover when attempting to promote a standby database. Check the error message for more details. 

If this occurs, the failover or switchover operation attempts to roll back to the old primary database. If the rollback fails, you may need to manually repair, restart, or recreate this database cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
