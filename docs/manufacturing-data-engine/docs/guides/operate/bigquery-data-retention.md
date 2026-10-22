---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/bigquery-data-retention/
title: BigQuery data retention \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:46.512764+00:00
---

# BigQuery data retention  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/bigquery-data-retention/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# BigQuery data retention

This guide describes how to configure data retention on BigQuery tables.

Depending on the Manufacturing Data Engine (MDE) operations log level a lot of data may be stored in the [operations-log](https://docs.cloud.google.com/manufacturing-data-engine/docs/reference/bigquery-schemas#operations_logs) BigQuery table. Since MDE is using partitioned tables you can manage retention as described in the [Managing partitioned tables](https://docs.cloud.google.com/bigquery/docs/managing-partitioned-tables) guide.

## Update the partition expiration example

You can use the `ALTER TABLE` `SET OPTIONS` statement to update the expiration as the following example shows:
    
    
    ALTER TABLE mde_system.operations-log
      SET OPTIONS (
        -- Sets partition expiration to 30 days
        partition_expiration_days = 30);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
