---
url: https://docs.cloud.google.com/spanner/docs/key-visualizer/metrics/
title: Key Visualizer metrics \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:19.521099+00:00
---

# Key Visualizer metrics  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/key-visualizer/metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)



Send feedback 

#  Key Visualizer metrics Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the metrics that you can view in Key Visualizer heatmaps.

## Metrics

Key Visualizer automtically captures and aggregates metrics about performance and resource usage for Spanner databases that have enabled it. All metrics in Key Visualizer are normalized by the number of rows. This means that the metric value inside a row range is the aggregated count divided by the number of rows inside the range.

Metrics | Description  
---|---  
CPU seconds | Number of CPU seconds spent per (wall clock) second reading / writing in a row range.  
Logical stored bytes | Bytes used to store data in a row range.  
Number of rows read | Number of rows read per second from a row range.  
Number of bytes read | Number of bytes read (not bytes returned) per second from a row range.  
Number of rows written | Number of rows inserted / updated per second in a row range.  
Number of bytes written | Number of bytes inserted / updated per second in a row range.  
  
## Time window granularity

Spanner Key Visualizer aggregates metrics at several different granularities over time. The most recent data is aggregated at the finest granularity, while earlier data is aggregated more coarsely.

Period | Granularity  
---|---  
Past 6 hours | 1 minute  
Past 4 days | 10 minutes  
Past 28 days | 1 hour  
  
## Data retention and wipeout

Spanner stores key ranges and metrics in an internal metadata table as part of the user's database. Spanner Key Visualizer data retention is as follows:

  * Data that is collected every minute will be deleted after six hours.
  * Data that is collected every ten minutes will be deleted after four days.
  * Data that is collected every hour will be deleted after 28 days.



Key Visualizer stores row key data in the metadata table. If your data retention requirements aren't compatible with Key Visualizer's data retention schedule, you can [disable Key Visualizer](https://docs.cloud.google.com/spanner/docs/key-visualizer/getting-started#enabling_key_visualizer).

## Limitations

There are some situations in which new data might not be immediately available in Key Visualizer.

  * Storage and traffic statistics for newly created databases might not be available immediately.
  * Traffic statistics for newly inserted rows might be attributed to existing key ranges.



## What's next

  * [Get started with Key Visualizer](https://docs.cloud.google.com/spanner/docs/key-visualizer/getting-started).
  * Learn [how Key Visualizer displays data in heatmaps](https://docs.cloud.google.com/spanner/docs/key-visualizer/exploring-heatmaps#heatmaps).
  * Find out [how to explore Key Visualizer heatmaps](https://docs.cloud.google.com/spanner/docs/key-visualizer/exploring-heatmaps).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
