---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/szpt/
title: Single Zone Provisioned Throughput \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:42:08.311062+00:00
---

# Single Zone Provisioned Throughput  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/szpt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Single Zone Provisioned Throughput Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** Single Zone Provisioned Throughput is **not** a Covered Service under the Monthly Latency Target Attainment Percentage SLO in the [Gemini Online Inference API on Gemini Enterprise Agent Platform Service Level Agreement](https://cloud.google.com/vertex-ai/generative-ai/sla).

Single Zone Provisioned Throughput lets you reserve throughput in specific regions where only one [zone](https://docs.cloud.google.com/docs/geography-and-regions) is available. This option provides predictable performance for Gemini models in use cases where ML processing is required.

To view the list of supported models and regions, see [Deployments and endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations). For the list of regions and models that support ML processing, see [ML processing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations#canada).

## Features of Single Zone Provisioned Throughput

This section outlines the key features of Single Zone Provisioned Throughput:

  * **Pricing and units are consistent with standard Provisioned Throughput** : Single Zone Provisioned Throughput uses the same measure of throughput ([GSUs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/measure-provisioned-throughput#gsu-burndown-rate)), [pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#provisioned-throughput), and terms as standard [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/purchase-provisioned-throughput).

  * **Single Zone Provisioned Throughput supports in-region ML processing** : All requests are processed in the purchased region, including traffic that exceeds your purchased amount of throughput. This traffic is billed at the [pay-as-you-go rate](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#provisioned-throughput) using buffer capacity in the region.

  * **You control the overages** : You can [control overflow traffic](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/use-provisioned-throughput#use-rest-api) using the same headers as with standard Provisioned Throughput.

  * **You can monitor your order** : You can monitor your Single Zone Provisioned Throughput order using the existing [Provisioned Throughput monitoring](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/use-provisioned-throughput#monitor_provisioned_throughput) capabilities.




## Limitations

Single Zone Provisioned Throughput has the following limitations:

  * Single Zone Provisioned Throughput is **not** a Covered Service under the Monthly Latency Target Attainment Percentage SLO in the [Gemini Online Inference API on Gemini Enterprise Agent Platform Service Level Agreement](https://cloud.google.com/vertex-ai/generative-ai/sla).

  * Single Zone Provisioned Throughput doesn't integrate with or support [fine-tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tune-models).

  * In regions without ML processing, latency for Single Zone Provisioned Throughput might be higher than standard Provisioned Throughput or pay-as-you-go.




## Purchase Single Zone Provisioned Throughput

For assistance with purchasing Single Zone Provisioned Throughput, [contact your Google Cloud account representative](https://cloud.google.com/contact).

## What's next

  * [Purchase standard Provisioned Throughput.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/purchase-provisioned-throughput)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
