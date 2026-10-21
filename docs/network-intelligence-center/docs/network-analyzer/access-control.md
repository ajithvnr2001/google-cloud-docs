---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/access-control/
title: Roles and permissions \u00a0|\u00a0 Network Intelligence Center - Network Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:40:55.358510+00:00
---

# Roles and permissions  |  Network Intelligence Center - Network Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview)



Send feedback 

#  Roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the permissions that you need to access Network Analyzer.

To access the analysis results of a project, you must have `compute.networks.list` and `compute.instances.list` permissions.

To access the analysis results of monitored projects of a Cloud Monitoring metrics scope, you must have `compute.networks.list` and `compute.instances.list` permissions on the scoping project of the metrics scope. On the Network Analyzer console of the scoping project, you can see the analysis results of all the monitoring projects.

## Access Network Analyzer logs in Cloud Logging

Network Analyzer writes insights as [platform logs](https://docs.cloud.google.com/logging/docs/api/platform-logs#network_analyzer) within Cloud Logging. You can access Network Analyzer logs by using the following options: the [Cloud Logging API](https://docs.cloud.google.com/logging/docs/reference/v2/rest), the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), and the [Google Cloud CLI](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging).

  * To receive Network Analyzer logs, you must enable the Logging API. For more information, see [Enable the Logging API](https://docs.cloud.google.com/logging/docs/api/enable-api).
  * To access the logs data in the [Logging API](https://docs.cloud.google.com/logging/docs/reference/v2/rest), the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), and the [gcloud CLI](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging), you must grant the required Identity and Access Management (IAM) roles and permissions. For more information, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).



## Access Network Analyzer insights in Recommender API

To access insights by using the Recommender API and the gcloud CLI, perform the following tasks:

  1. Enable the [Recommender API](https://docs.cloud.google.com/recommender/docs/overview) for your project.
  2. Grant the required IAM roles and permissions to access Network Analyzer insight types in the Recommender API. For more information, see [Recommender roles](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
