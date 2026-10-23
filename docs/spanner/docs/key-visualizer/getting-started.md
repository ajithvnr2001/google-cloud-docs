---
url: https://docs.cloud.google.com/spanner/docs/key-visualizer/getting-started/
title: Access Key Visualizer \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:45.329709+00:00
---

# Access Key Visualizer  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/key-visualizer/getting-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Access Key Visualizer Stay organized with collections  Save and categorize content based on your preferences. 

Key Visualizer is enabled in Spanner by default.

## Before you begin

To view Key Visualizer, you need the following [Identity and Access Management (IAM) permission](https://docs.cloud.google.com/spanner/docs/iam):

  * `spanner.databases.read`



If you are a fine-grained access control user, you must have been granted access to:

  * the `spanner_sys_reader` system role or one of its member roles.



For more information, see [About fine-grained access control](https://docs.cloud.google.com/spanner/docs/fgac-about) and [Fine-grained access control system roles](https://docs.cloud.google.com/spanner/docs/fgac-system-roles).

## Access the Key Visualizer interface

You access the Key Visualizer tool from the [Google Cloud console](https://console.cloud.google.com/).

To access Key Visualizer:

  1. From the [Spanner page](https://console.cloud.google.com/spanner/) of the Google Cloud console, select an instance.

  2. Select a database to investigate.

  3. In the navigation menu, under **Observability** , select **Key Visualizer**.




## Disable Key Visualizer

Key Visualizer is controlled by the `enable_key_visualizer` database option. The default value is `true`.

To disable Key Visualizer, set the value of the `enable_key_visualizer` database option to `false`. The DDL syntax to disable Key Visualizer is:
    
    
    ALTER DATABASE `database_id` SET OPTIONS (enable_key_visualizer=false)
    

If your database ID contains characters other than letters, numbers, or underscores, be sure to enclose the ID with backticks (``).

The statement can be sent using a gcloud command, or in an `UpdateDatabaseDdl` gRPC/REST request. For example:
    
    
    gcloud spanner databases ddl update database_id --instance=instance_id \
        --ddl='ALTER DATABASE `database_id` SET OPTIONS ( enable_key_visualizer=false )'
    

Once you've explicitly set the value for `enable_key_visualizer`, you can check its value by clicking **SHOW EQUIVALENT DDL** in the overview page, or using the `ddl describe` gcloud command:
    
    
    gcloud spanner databases ddl describe `database_id` --instance=instance_id
    

## Re-enable Key Visualizer

To re-enable Key Visualizer, follow the previous instructions, setting the value of the `enable_key_visualizer` database option to `true`.

When first re-enabled for a database, the Key Visualizer heatmap will be empty for the first few minutes while Spanner collects metrics.

## What's next

  * Learn to recognize [common patterns in heatmaps](https://docs.cloud.google.com/spanner/docs/key-visualizer/patterns).
  * Find out how to [explore a heatmap in depth](https://docs.cloud.google.com/spanner/docs/key-visualizer/exploring-heatmaps).
  * Read about the [metrics you can view in a heatmap](https://docs.cloud.google.com/spanner/docs/key-visualizer/metrics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
