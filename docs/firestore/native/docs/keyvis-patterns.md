---
url: https://docs.cloud.google.com/firestore/native/docs/keyvis-patterns/
title: Heatmap patterns for document keys \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:45.183909+00:00
---

# Heatmap patterns for document keys  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/keyvis-patterns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/native/docs/create-database-server-client-library)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Heatmap patterns for document keys

This page shows examples of patterns that you might see in a Key Visualizer heatmap. These patterns can help you troubleshoot specific performance issues.

### Edition and mode requirements

This document applies to Firestore Standard edition in Firestore in Native mode. 

## Evenly distributed usage

![Heatmap showing evenly distributed reads and writes](https://docs.cloud.google.com/static/firestore/native/docs/images/keyvis-patterns-ideal.png)

If a heatmap shows a fine-grained mix of dark and bright colors, then reads and writes are evenly distributed throughout the database. This heatmap likely represents an effective usage pattern for Firestore.

## Sequential keys

![Example heatmap showing a diagonal hot band](https://docs.cloud.google.com/static/firestore/native/docs/images/monotonically-increasing-keys.png)

A heatmap with a single bright diagonal line can indicate a database that uses strictly increasing or decreasing keys. Sequential keys are an anti-pattern that can create hotspots. To learn more about hotspots, see the [best practices page](https://docs.cloud.google.com/firestore/docs/best-practices#high_read_write_and_delete_rates_to_a_narrow_document_range).

When hotspotting, you might observe corresponding elevated latencies when you compare a `Ops/s` metric with a latency metric.

## Sudden traffic increase

![Heatmap showing a sudden increase](https://docs.cloud.google.com/static/firestore/native/docs/images/keyvis-patterns-inflection.png)

A heatmap with a key range that suddenly changes from dark to bright indicates a sudden spike in load. If `Ops` traffic increases faster than Firestore can auto-scale resources, you might see corresponding elevated `latency` metrics.

## What's next

  * Learn how to [get started with Key Visualizer](https://docs.cloud.google.com/firestore/native/docs/keyvis-getting-started).
  * Find out how to [explore a heatmap in detail](https://docs.cloud.google.com/firestore/native/docs/keyvis-exploring-heatmaps).
  * Read about the [metrics you can view in a heatmap](https://docs.cloud.google.com/firestore/native/docs/key-visualizer#metrics).
  * Learn about [index key patterns](https://docs.cloud.google.com/firestore/native/docs/keyvis-patterns-index)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
