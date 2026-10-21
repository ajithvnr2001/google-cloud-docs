---
url: https://docs.cloud.google.com/recommender/docs/transparency-and-control-center/exporting-data/
title: Data export in Transparency and Control Center \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:53.778258+00:00
---

# Data export in Transparency and Control Center  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/transparency-and-control-center/exporting-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Guides ](https://docs.cloud.google.com/recommender/docs/whatis-activeassist)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Data export in Transparency and Control Center 

## Overview

Transparency and Control Center uses [BigQuery](https://docs.cloud.google.com/bigquery-transfer/docs/introduction) to export data for specific data processing groups at either the project or organization level. To export data for the remaining recommendations, refer to the [documentation for each recommender](https://docs.cloud.google.com/recommender/docs/recommenders).

## Required permissions

To manage data source exports, you must have the following Identity and Access Management (IAM) role on the project or organization:

  * Data Processing Controls Resource Admin (`roles/dataprocessing.admin`), or an equivalent custom IAM role



Additionally, you must have the following IAM role on the project you will be exporting to:

  * BigQuery Admin (`roles/bigquery.admin`)

**Note:** For more information about roles, refer to [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles) and [Granting, changing, and revoking access](https://cloud.google.com/iam/docs/granting-changing-revoking-access).

## Export data from Transparency and Control Center

To export data from Transparency and Control Center, complete the following steps:

  1. In the Google Cloud console, go to the **Privacy & Security** page.

[Go to the Privacy & Security page](https://console.cloud.google.com/iam-admin/privacy)

  2. Click **Transparency & control**.

  3. In the **Data processing group** table, click a group's name to see its details page.

  4. On the details page, find the data source you want to transfer and click **Create transfer**.




In the panel displayed, you can select a destination project, schedule a recurring transfer, and adjust notification options. When finished, your transfer settings are visible on the data processing group's details page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
