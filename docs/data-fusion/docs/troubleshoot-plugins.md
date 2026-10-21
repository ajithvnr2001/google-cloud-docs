---
url: https://docs.cloud.google.com/data-fusion/docs/troubleshoot-plugins/
title: Troubleshoot Cloud Data Fusion plugins \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:39.433329+00:00
---

# Troubleshoot Cloud Data Fusion plugins  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/troubleshoot-plugins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Troubleshoot Cloud Data Fusion plugins Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to resolve common issues encountered when using plugins in Cloud Data Fusion.

## Concatenated GZIP files fail to decompress

In Cloud Data Fusion version 6.10.1 and later, the Decompress plugin might not fully process concatenated GZIP (`.gz`) archives.

To resolve this issue, update the Decompress plugin to version 1.2.1 or later from the Hub.

## Cloud Storage Multi File sink plugin fails with Flexible schema

In Cloud Data Fusion version 6.10.1 and later, pipelines using the Cloud Storage Multi File sink might fail when the **Flexible schema** property is set to `true`

To resolve this issue, update the Cloud Storage Multi File sink plugin to version 0.23.2 or later from the Hub.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
