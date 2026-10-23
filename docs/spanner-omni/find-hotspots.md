---
url: https://docs.cloud.google.com/spanner-omni/find-hotspots/
title: Find hotspots in your Spanner Omni database \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:22.711332+00:00
---

# Find hotspots in your Spanner Omni database  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/find-hotspots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Find hotspots in your Spanner Omni database Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to diagnose hotspots, or queries with high CPU usage, in your Spanner Omni databases. The process for diagnosing hotspots is mostly identical to [Spanner hotspot diagnosis](https://docs.cloud.google.com/spanner/docs/find-hotspots-in-database), with the following distinctions:

  * The Spanner Omni system insights dashboard is available in Grafana. For more information on how to set up this dashboard, see [set up Grafana](https://docs.cloud.google.com/spanner-omni/deploy-on-vms#setup-grafana).

  * Instead of going to the Google Cloud console to query `SPANNER_SYS.*` tables, you query your database directly using the Spanner Omni CLI. For example, the following query shows the data splits with the highest CPU usage over the past 5 hours in the database, and ranks them by CPU usage:
        
        spanner sql \
        --database DATABASE_ID --execute \
        "SELECT * \
        FROM SPANNER_SYS.SPLIT_STATS_TOP_MINUTE \
        WHERE INTERVAL_END > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), \
        INTERVAL 5 HOUR) \
        ORDER BY CPU_USAGE_SCORE DESC"
        

Replace DATABASE_ID with the database identifier—for example, `MY_DATABASE`.




## Known issues

  * If the total compute capacity of your Spanner Omni deployment is less than 3.5 vCPU per server, the split CPU usage scores in the `SPANNER_SYS.*` tables might be lower than the correct scores on the system insights dashboard. The dashboard shows the correct split CPU usage scores, but you need to query the `SPANNER_SYS.*` tables to identify the splits that correspond to those scores.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
