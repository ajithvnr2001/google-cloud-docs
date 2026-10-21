---
url: https://docs.cloud.google.com/tpu/docs/about-tpu-reservations/
title: About Cloud TPU reservations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:45:43.029988+00:00
---

# About Cloud TPU reservations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/about-tpu-reservations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About Cloud TPU reservations

This document explains how to reserve Cloud TPUs for your exclusive use by requesting one of the following:

  * A [future reservation for up to 90 days (in calendar mode)](https://docs.cloud.google.com/tpu/docs/calendar-mode-reservation)
  * A [future reservation for one year or longer with a committed use discount](https://docs.cloud.google.com/tpu/docs/long-term-reservation)



Reservations are useful for the following cases:

  * Planned or unplanned usage spikes
  * Obtaining high-demand resources
  * Long-running training jobs and inference workloads
  * Workloads requiring a high assurance of capacity



A reservation is one consumption option for Cloud TPU. For more information, see [Cloud TPU consumption options](https://docs.cloud.google.com/tpu/docs/consumption-options).

**Note:** If you want to request a reservation in All Capacity mode, you must use the [request an All Capacity mode reservation](https://docs.cloud.google.com/tpu/docs/request-all-capacity-mode-reservation) flow. For more information, see [All Capacity mode overview](https://docs.cloud.google.com/tpu/docs/all-capacity-overview).

## Choose a reservation type

To choose the best reservation type for your needs, consider the duration of your workload and whether you want to commit to a longer-term usage agreement in exchange for higher discounts:

  * **Short-term workloads:** Choose a future reservation for up to 90 days (calendar mode) if you need capacity for planned, time-bound events, such as short-term training tasks or seasonal spikes in user demand.
  * **Long-term workloads:** Choose a future reservation for one year or longer if you have steady, predictable workloads that run continuously and want to take advantage of committed use discounts (CUDs).



Both reservation types give you a high level of assurance that TPUs are available when you need them, for a specified time period. The following table shows the differences between the reservation types:

| Future reservations for up to 90 days (in calendar mode) | Future reservations for one year or longer | Duration | 1 to 90 days | 1 to 3 years  
---|---|---  
Supported TPU versions | v5p, v6e, and TPU7x | All TPU versions  
Cost (for more information, see [DWS pricing](https://cloud.google.com/products/dws/pricing)) | Up to 30% less than on-demand | 30% to 55% less than on-demand  
How to request | Self-service using the Compute Engine API or the Google Cloud console | Manual process through [Cloud Sales](https://cloud.google.com/contact) or your [account manager](https://cloud.google.com/tam)  
Committed use discount (CUD) | Not supported | CUD required  
  
### Create a reservation

Depending on the reservation type you choose, you request and create the reservation in one of the following ways:

  * **For future reservations up to 90 days (calendar mode):** You request a future reservation yourself using the Google Cloud CLI, Compute Engine API, or Google Cloud console. For more details, see [Request a future reservation for up to 90 days in calendar mode](https://docs.cloud.google.com/tpu/docs/calendar-mode-reservation).
  * **For future reservations of one year or longer (CUD):** To request a long-term future reservation, you must purchase a committed use discount (CUD). You request these reservations manually by contacting [Cloud Sales](https://cloud.google.com/contact) or your account manager. For more details, see [Request a future reservation for one year or longer](https://docs.cloud.google.com/tpu/docs/long-term-reservation).



## What's next

  * [Request a future reservation for up to 90 days in calendar mode](https://docs.cloud.google.com/tpu/docs/calendar-mode-reservation)
  * [Request a future reservation for one year or longer](https://docs.cloud.google.com/tpu/docs/long-term-reservation)
  * [Share a reservation between projects](https://docs.cloud.google.com/tpu/docs/share-reservation)
  * After your reservation start date, [consume the reservation](https://docs.cloud.google.com/tpu/docs/consume-reservation-compute)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
