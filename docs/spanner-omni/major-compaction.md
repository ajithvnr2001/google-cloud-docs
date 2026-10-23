---
url: https://docs.cloud.google.com/spanner-omni/major-compaction/
title: Manually trigger major compaction in a Spanner Omni database \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:46.072785+00:00
---

# Manually trigger major compaction in a Spanner Omni database  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/major-compaction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Manually trigger major compaction in a Spanner Omni database Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to manually trigger a major compaction in your Spanner Omni database. This process is mostly identical to [triggering a major compaction in a Spanner database](https://docs.cloud.google.com/spanner/docs/manual-data-compaction), with the following distinction:

  * To trigger a major compaction for a Spanner Omni database, use the following command in the Spanner Omni CLI:
        
        spanner admin alpha compact database DATABASE_ID
        

Replace DATABASE_ID with the database identifier—for example, `MY_DATABASE`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
