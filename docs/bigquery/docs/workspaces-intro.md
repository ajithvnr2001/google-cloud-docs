---
url: https://docs.cloud.google.com/bigquery/docs/workspaces-intro/
title: Introduction to workspaces \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:16.945144+00:00
---

# Introduction to workspaces  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/workspaces-intro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Introduction to workspaces

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** To provide feedback or ask questions that are related to this Preview feature, contact [bigquery-repositories-feedback@google.com](mailto:%20bigquery-repositories-feedback@google.com).

Workspaces in BigQuery let you edit and manage code stored in [repositories](https://docs.cloud.google.com/bigquery/docs/repository-intro). Within a workspace, you can create and modify files while the parent repository uses Git to record changes and manage file versions.

## View workspaces

On the BigQuery page, your workspaces are displayed in alphabetical order under the repository they are associated with. To view repositories, do the following:

  1. In the left pane, click explore **Explorer** :

![Highlighted button for the Explorer pane.](https://docs.cloud.google.com/static/bigquery/images/explorer-tab.png)

If you don't see the left pane, click last_page **Expand left pane** to open the pane.

  2. In the **Explorer** pane, click **Repositories**.




## Supported file types

You can create or upload the following types of files to a repository:

  * SQL queries
  * Python notebooks
  * [Data canvases](https://docs.cloud.google.com/bigquery/docs/data-canvas)
  * [Data preparations](https://docs.cloud.google.com/bigquery/docs/data-prep-introduction)
  * Any other types of files



For more information, see [Work with files in a workspace](https://docs.cloud.google.com/bigquery/docs/workspaces#work_with_files_in_a_workspace).

## Git integration

As you create and modify files in a workspace, you can perform Git actions like committing changes and pushing changes to the repository. For more information, see [Use version control with a file](https://docs.cloud.google.com/bigquery/docs/workspaces#use_version_control_with_a_file).

## Locations

Each workspace uses the same [location](https://docs.cloud.google.com/bigquery/docs/repository-intro#locations) as the repository that contains it.

## Quotas

[Dataform quotas](https://docs.cloud.google.com/dataform/docs/quotas#quotas) apply to use of BigQuery workspaces.

## Pricing

You are not charged for creating, updating, or deleting a workspace, or for storage of the files in a workspace.

For more information on BigQuery pricing, see [Pricing](https://cloud.google.com/bigquery/pricing).

## What's next

  * To learn how to create and use repositories, see [Create a repository](https://docs.cloud.google.com/bigquery/docs/repositories).
  * To learn how to create and use workspaces, see [Create a workspace](https://docs.cloud.google.com/bigquery/docs/workspaces).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
