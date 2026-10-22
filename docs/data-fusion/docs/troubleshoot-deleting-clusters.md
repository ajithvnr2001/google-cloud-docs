---
url: https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters/
title: Troubleshoot deleting clusters \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:56.924031+00:00
---

# Troubleshoot deleting clusters  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/troubleshoot-deleting-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Troubleshoot deleting clusters Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with deleting ephemeral Managed Service for Apache Spark clusters in Cloud Data Fusion.

When Cloud Data Fusion creates an ephemeral Managed Service for Apache Spark cluster during pipeline run provisioning, the cluster gets deleted after the pipeline run is finished. In rare cases, the cluster deletion fails.

**Strongly recommended** : Upgrade to the most recent Cloud Data Fusion version to ensure proper cluster maintenance.

## Skip cluster deletion

For debugging purposes, you can stop the automatic deletion of an ephemeral cluster.

To stop the deletion, set the `Skip Cluster Deletion` property to `True`. You must manually delete the cluster after you finish debugging.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
