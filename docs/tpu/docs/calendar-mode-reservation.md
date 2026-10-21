---
url: https://docs.cloud.google.com/tpu/docs/calendar-mode-reservation/
title: Request a future reservation for up to 90 days (in calendar mode) \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:39:20.126898+00:00
---

# Request a future reservation for up to 90 days (in calendar mode)  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/calendar-mode-reservation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Request a future reservation for up to 90 days (in calendar mode)

To reserve TPUs for a specific start time and duration, between 1 and 90 days, request a future reservation in calendar mode. This mode, powered by the [Dynamic Workload Scheduler](https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler), lets you check TPU availability up to 120 days in advance and request capacity based on your schedule. You can request a future reservation in calendar mode using the Compute Engine API or Google Cloud console. If approved, Compute Engine automatically creates a reservation for your chosen date and time. You can then [consume the reservation](https://docs.cloud.google.com/tpu/docs/consume-reservation-compute) by provisioning TPUs, such as VM instances or MIGs, using the Compute Engine API. Compute Engine automatically deletes the reservation, and any TPUs that consume it, at the end of your reservation period.

Requesting a future reservation for up to 90 days (in calendar mode) is a good fit for training and experimentation workloads that require precise start times and have a defined duration.

For more information, see [About future reservation requests in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview).

## View future availability of TPUs

You can view the availability of TPUs 1 to 120 days in advance. For more information, see [View resources future availability](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode#view-availability).

## Create a future reservation request in calendar mode

You can request a future reservation in calendar mode using the Compute Engine API or Google Cloud console. For more information, see [Create a future reservation request in calendar mode](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode).

## Limitations

Requesting a future reservation in calendar mode for TPUs has the following limitations:

  * You can't modify a future reservation request.
  * You must specify a reservation duration with a minimum of 1 day and a maximum of 90 days.
  * You can reserve 1, 4, 8, 16, 32, 64, 128, 256, 512, or 1,024 TPU chips per request.
  * You can only reserve the following TPU versions: 
    * [TPU7x](https://docs.cloud.google.com/tpu/docs/tpu7x)
    * [TPU v6e](https://docs.cloud.google.com/tpu/docs/v6e)
    * [TPU v5p](https://docs.cloud.google.com/tpu/docs/v5p)
  * You can reserve TPUs only in specific [regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones).

**Important:** If TPU chips aren't available in any region after you [ view future availability](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode#view-availability), then contact your account team or the sales team. 



## What's next

  * [Learn about Cloud TPU reservations](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations)
  * [Share a reservation between projects](https://docs.cloud.google.com/tpu/docs/share-reservation)
  * After your reservation start date, [consume the reservation](https://docs.cloud.google.com/tpu/docs/consume-reservation-compute)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
