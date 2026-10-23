---
url: https://docs.cloud.google.com/oracle/compute/plan-for-oracle-on-compute/
title: Plan for Oracle on Google Cloud Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:52.677299+00:00
---

# Plan for Oracle on Google Cloud Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/compute/plan-for-oracle-on-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Oracle on Google Cloud Compute ](https://docs.cloud.google.com/oracle/compute)
  * [ Guides ](https://docs.cloud.google.com/oracle/compute/overview)



Send feedback 

#  Plan for Oracle on Google Cloud Compute Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the key requirements to help you decide how to deploy Oracle Database workloads in Google Cloud.

## Operating systems

Oracle on Google Cloud Compute lets you run any Linux operating system that's supported by Oracle, including the following operating systems:

  * Red Hat Enterprise Linux versions 7, 8, and 9
  * Oracle Linux versions 7, 8, and 9



## Oracle versions

Oracle on Google Cloud Compute supports the following Oracle versions:

  * Oracle Database 19c
  * Oracle Database 23ai



## Oracle editions

Oracle on Google Cloud Compute supports the following Oracle editions:

  * Enterprise Edition
  * Standard Edition
  * Express (Free) Edition



## Compute Engine machine types

You can choose Compute Engine machine types based on your workload requirements:

  * For basic and less-demanding Oracle Database workloads, you can use the following general-purpose machine types:

    * N4 series
    * C4 series

For more information, see [General-purpose machine family for Compute Engine](https://docs.cloud.google.com/compute/docs/general-purpose-machines).

  * For complex and memory-intensive Oracle Database workloads, you can use the following memory-optimized machine types:

    * M4N series

For more information, see [Google Cloud blog about What's new with compute: Scaling core and agentic workloads](https://cloud.google.com/blog/products/compute/whats-new-in-compute-at-next26).




## Storage

You can use [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced) or [Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme) with the supported machine types based on the input and output operations per second (IOPS) and throughput requirements of your Oracle Database workloads.

Oracle Databases require [steady state performance](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-performance#steady-state). Therefore, we recommend reviewing the [Performance limits for machine types with steady state performance](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#steady-state) before choosing a storage option.

## Supported regions

Oracle on Google Cloud Compute supports regions where N4, C4, and M4N machine types are available. The list of available regions might change depending on the number of machines available for you to use.

For more information, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
