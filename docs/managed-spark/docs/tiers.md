---
url: https://docs.cloud.google.com/managed-spark/docs/tiers/
title: Managed Service for Apache Spark tiers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:55.010261+00:00
---

# Managed Service for Apache Spark tiers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/tiers/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark tiers Stay organized with collections  Save and categorize content based on your preferences. 

Managed Service for Apache Spark offers two tiers, a **standard** tier and a **premium** (high performance) tier, to allow customers to align performance requirements and feature access with optimal cost.

## Premium tier benefits

The premium tier is differentiated from the standard tier by its added capabilities and features. The premium tier provides advanced query acceleration, and accelerated compute, disk and memory often required by complex or latency-sensitive workloads.

**Note:** The average startup time for both standard and premium tier batches and sessions is `40` to `50` seconds. Startup times can be greater when using [custom containers](https://docs.cloud.google.com/managed-spark/docs/guides/custom-containers).

### Premium tier features and capabilities

The following table highlights the Managed Service for Apache Spark exclusive premium tier features and capabilities.

Feature | Standard | Premium  
---|---|---  
[**Lightning Engine (Query Acceleration)**](https://docs.cloud.google.com/managed-spark/docs/guides/native-query-execution) | ![Remove Icon](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/remove/default/24px.svg) |  (Default: Enabled, except for interactive sessions)  
[**Interactive Workloads (Sessions)**](https://docs.cloud.google.com/managed-spark/docs/guides/create-serverless-sessions-templates) | ![Remove Icon](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/remove/default/24px.svg) |  (Default: Enabled)  
[**Shuffle-Intensive Jobs (premium Disk)**](https://docs.cloud.google.com/managed-spark/docs/concepts/properties#resource_allocation_properties) | ![Remove Icon](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/remove/default/24px.svg) |  (Default: Disabled)  
[**Memory-Intensive Jobs (Extended Memory)**](https://docs.cloud.google.com/managed-spark/docs/concepts/properties#resource_allocation_properties) | ![Remove Icon](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/remove/default/24px.svg) |  (Default: Disabled)  
[**GPU Support**](https://docs.cloud.google.com/managed-spark/docs/guides/gpus-serverless) | ![Remove Icon](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/remove/default/24px.svg) |  (Default: Disabled)  
[**Batch workloads**](https://docs.cloud.google.com/managed-spark/docs/overview#spark-batch) |  |   
[**Autoscaling**](https://docs.cloud.google.com/managed-spark/docs/concepts/autoscaling) |  |   
[**Serverless Spark UI**](https://docs.cloud.google.com/managed-spark/docs/guides/monitor-troubleshoot-batches#spark_ui) |  |   
**[Lineage](https://docs.cloud.google.com/managed-spark/docs/guides/data-lineage), Security and Compliance** ([VPC-SC](https://docs.cloud.google.com/managed-spark/docs/concepts/network#s8s-and-vpc-sc-networks), [CMEK](https://docs.cloud.google.com/managed-spark/docs/guides/cmek-serverless)) |  |   
  
## Premium tier batch workloads and sessions

The following workloads and sessions require the premium tier:

  * **Lightning Engine:** Exclusively available in the premium tier, [Lightning Engine](https://docs.cloud.google.com/managed-spark/docs/guides/lightning-engine) is a critical feature that accelerates Spark performance through optimized query execution. It is enabled by default when you select the premium tier for batch workloads by setting the `dataproc.tier` property to `premium`.
  * **Interactive sessions:** Interactive sessions are automatically treated as a high-value, premium feature. They are initiated through the Managed Service for Apache Spark sessions API, and are charged at the premium DCU rate, providing capabilities such as low latency interactivity and state management. For interactive sessions, you enable Lightning Engine by setting the `spark.dataproc.engine` property to `lightningEngine`.
  * **GPU support:** GPU support is available only in the premium tier. It is disabled by default. You enable it through configuration flags. GPU support uses specialized infrastructure, and is covered by the premium DCU rate with no additional compute cost.



## Predictable premium tier pricing model

The premium tier uses a simplified, all-inclusive pricing model for its core capabilities. The [premium DCU rate](https://cloud.google.com/products/managed-service-for-apache-spark/pricing) covers access to high-value features such as Lightning Engine, Extended Memory, and the specialized infrastructure needed for shuffle-intensive jobs. When you enable these features through configuration flags, they are included in the base premium DCU rate and **incur no additional compute cost**. This means you pay a single, predictable premium rate for access to the complete suite of premium tier advanced capabilities.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
