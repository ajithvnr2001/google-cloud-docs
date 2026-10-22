---
url: https://docs.cloud.google.com/dataproc-metastore/docs/scaling-factors/
title: Dataproc Metastore scaling factors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:38.471693+00:00
---

# Dataproc Metastore scaling factors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/scaling-factors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Dataproc Metastore scaling factors Stay organized with collections  Save and categorize content based on your preferences. 

When you create a Dataproc Metastore service, you can choose to use a _Dataproc Metastore 2 service_ or a _Dataproc Metastore 1 service_.

This document explains how to control resource consumption for Dataproc Metastore 2.

## Scaling factors and editions

Dataproc Metastore 2 uses _scaling factors_ and _editions_ (workloads) to handle varying levels of stability and workloads. You select your scaling factor and edition when you create a Dataproc Metastore service.

After you create your Dataproc Metastore service, you can scale the service up or down by modifying the scaling factor. Scaling factors range from `small` to `XLarge` and are represented by a number ranging from `0.1` to `6.0`.

For more information about editions and scaling factors, see [Scaling factors and workloads](https://docs.cloud.google.com/dataproc-metastore/pricing#service-2-scaling).

## Autoscaling

Dataproc Metastore 2 also supports autoscaling. If you turn on autoscaling, you set a minimum scaling factor and a maximum scaling factor. After these parameters are set, your service automatically increases or decreases resource consumption to run workloads. Autoscaling is only available for single-region Dataproc Metastore instances.

For more information on setting up autoscaling, see [Create an autoscaling service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service#autoscaling).

## Resource constrained regions

Dataproc Metastore is present in several regions that have fewer resources available than others. These regions constrain the maximum scaling factor to `1` and don't support autoscaling. The following regions are considered resource-constrained regions by Dataproc Metastore:

  * `australia-southeast2`
  * `europe-southwest1`
  * `europe-west8`
  * `europe-west9`
  * `europe-west12`
  * `southamerica-west1`
  * `us-east5`
  * `us-south1`
  * `me-central1`
  * `me-central2`
  * `me-west1`



## What's next

  * [Create a service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service)
  * [Release notes](https://docs.cloud.google.com/dataproc-metastore/docs/release-notes)
  * [Version policy](https://docs.cloud.google.com/dataproc-metastore/docs/version-policy)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
