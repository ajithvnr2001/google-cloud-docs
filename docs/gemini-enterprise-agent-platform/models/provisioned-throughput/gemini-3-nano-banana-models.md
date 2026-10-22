---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/gemini-3-nano-banana-models/
title: Provisioned Throughput for Gemini Nano Banana models \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:42:08.553902+00:00
---

# Provisioned Throughput for Gemini Nano Banana models  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/gemini-3-nano-banana-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Provisioned Throughput for Gemini Nano Banana models Stay organized with collections  Save and categorize content based on your preferences. 

This section explains how Provisioned Throughput works for Gemini Image (also known as Nano Banana) models, including quota enforcement behavior and minimum GSU purchase increment.

For [Gemini Image models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/image-generation), the [quota enforcement windows](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/use-provisioned-throughput#pt-quota-enforcement-period) vary based on the number of GSUs you purchase for the model, and are subject to change. The following sections list quota enforcement windows for different GSU sizes.

## Gemini Nano Banana 2.1

The following are the quota enforcement windows for different GSU sizes for Gemini Nano Banana 2.1:

  * 1 GSU: 615 seconds
  * 2 GSUs: 310 seconds
  * 3 GSUs: 205 seconds
  * 4 GSUs: 155 seconds
  * 5 GSUs: 125 seconds
  * 6 GSUs: 105 seconds
  * 7-20 GSUs: 100 seconds
  * 21-24 GSUs: 30 seconds
  * 25-30 GSUs: 25 seconds
  * 31-40 GSUs: 20 seconds
  * 41-61 GSUs: 15 seconds
  * 62-122 GSUs: 10 seconds
  * 123+ GSUs: 5 seconds



## Gemini 3.1 Flash-Lite Image

The following are the quota enforcement windows for different GSU sizes for Gemini 3.1 Flash-Lite Image:

  * 1 GSU: 100 seconds
  * 2 GSUs: 50 seconds
  * 3 GSUs: 35 seconds
  * 4 GSUs: 25 seconds
  * 5 GSUs: 20 seconds
  * 6-12 GSUs: 15 seconds
  * 13-24 GSUs: 10 seconds
  * 25+ GSUs: 5 seconds



## Gemini 3 Pro Image

The following are the quota enforcement windows for different GSU sizes for Gemini 3 Pro Image:

  * 1 GSU: 1,230 seconds
  * 2 GSUs: 615 seconds
  * 3 GSUs: 410 seconds
  * 4 GSUs: 310 seconds
  * 5 GSUs: 245 seconds
  * 6 GSUs: 205 seconds
  * 7-12 GSUs: 175 seconds
  * 13-24 GSUs: 100 seconds
  * 25-30 GSUs: 50 seconds
  * 31-40 GSUs: 40 seconds
  * 41-61 GSUs: 30 seconds
  * 62-122 GSUs: 20 seconds
  * 123-244 GSUs: 10 seconds
  * 245+ GSUs: 5 seconds



## Gemini 3.1 Flash Image

The following are the quota enforcement windows for different GSU sizes for Gemini 3.1 Flash Image:

  * 1 GSU: 435 seconds
  * 2 GSUs: 220 seconds
  * 3 GSUs: 145 seconds
  * 4 GSUs: 110 seconds
  * 5-14 GSUs: 100 seconds
  * 15-17 GSUs: 30 seconds
  * 18-21 GSUs: 25 seconds
  * 22-28 GSUs: 20 seconds
  * 29-42 GSUs: 15 seconds
  * 43-99 GSUs: 10 seconds
  * 100+ GSUs: 5 seconds



## Gemini 2.5 Flash Image

The following are the quota enforcement windows for different GSU sizes for Gemini 2.5 Flash Image:

  * 1 GSU: 120 seconds
  * 2 GSUs: 60 seconds
  * 3 GSUs: 40 seconds
  * 4-693 GSUs: 30 seconds
  * 694+ GSUs: 5 seconds



The listed values aren't connected to the request latency. The time to process your request isn't the same as the quota enforcement window.

Enforcement windows are larger at smaller GSU amounts to ensure that smaller requests are processed successfully within the window. As the number of GSUs for a model increases, longer window times aren't required to process a request. To process outputs on Gemini Image models more frequently using Provisioned Throughput, increase the number of GSUs purchased and check the corresponding enforcement window.

For example, consider a situation where you purchased 1 GSU of Gemini Nano Banana 2.1 and have a workload that requires generating a single image with 4K resolution. In this case, you can usually generate this single image within seconds and the traffic is processed as Provisioned Throughput. However, to generate another image of the same size, you must wait until the quota enforcement window ends (615 seconds for 1 GSU). The time of this enforcement window is determined by the Gemini Enterprise Agent Platform clock time and not when the request is made.

Use the estimation tool on the [Provisioned Throughput page](https://console.cloud.google.com/agent-platform/provisioned-throughput/price-estimate) to estimate the number of GSUs required for your workload. For more information about using the estimation tool, see [Purchase a Provisioned Throughput order](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/purchase-provisioned-throughput#place-an-order).

## What's next

For more information, see the following:

  * [Purchase standard Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/purchase-provisioned-throughput#place-an-order)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
