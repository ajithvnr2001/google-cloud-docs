---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/serverless-staging-bucket/
title: Managed Service for Apache Spark staging buckets \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:23.031307+00:00
---

# Managed Service for Apache Spark staging buckets  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/serverless-staging-bucket/




#  Managed Service for Apache Spark staging buckets Stay organized with collections  Save and categorize content based on your preferences. 

This document provides information about Managed Service for Apache Spark staging buckets. Managed Service for Apache Spark creates a Cloud Storage staging bucket in your project or reuses an existing staging bucket from previous batch creation requests. This is the default bucket created by Managed Service for Apache Spark clusters. For more information, see [Managed Service for Apache Spark staging and temp buckets](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/staging-bucket).

Managed Service for Apache Spark stores workload dependencies, config files, and job driver console output in the staging bucket.

Managed Service for Apache Spark sets regional staging buckets in [Cloud Storage locations](https://docs.cloud.google.com/storage/docs/locations#location-r) according to the Compute Engine zone where your workload is deployed, and then creates and manages these project-level, per-location buckets. Managed Service for Apache Spark-created staging buckets are shared among workloads in the same region, and are created with a Cloud Storage [soft delete retention](https://docs.cloud.google.com/storage/docs/soft-delete#retention-duration) duration set to 0 seconds.

To locate the Managed Service for Apache Spark default staging bucket, in the Google Cloud console, go to **[Cloud Storage](https://console.cloud.google.com/storage/browser)** and filter the results using the `dataproc-staging-` prefix. 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
