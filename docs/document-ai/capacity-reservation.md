---
url: https://docs.cloud.google.com/document-ai/capacity-reservation/
title: Capacity reservation \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:10.406119+00:00
---

# Capacity reservation  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/capacity-reservation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Resources ](https://docs.cloud.google.com/document-ai/docs/resources)



Send feedback 

#  Capacity reservation Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the process to make a capacity reservation request for Document AI. Document AI capacity reservation provides reserved capacity to serve real-time, high-volume prediction traffic for the subscribed period, helping meet Service Level Agreement (SLA) requirements. Each unit corresponds to an additional page-per-minute beyond the default quota. Capacity reservation is supported and required for increasing provisioned tier quotas of [custom extractor](https://docs.cloud.google.com/document-ai/docs/ce-with-genai#models) models v1.4 and v1.5, including fine-tuned processor versions built on them. Pricing for capacity reservation is $300 USD for every extra page-per-minute per-month.

## Considerations before purchasing capacity reservation

To help you decide whether to purchase capacity reservation, consider the following:

  * **You can't cancel your order in the middle of your term.**

Your capacity reservation purchase is a commitment. However, you can increase the number of purchased pages per minute. If you accidentally purchase a commitment or there's a problem with your configuration, [contact your Google Cloud account representative](https://cloud.google.com/contact) for assistance.

  * **You can auto-renew your subscription.**

When you submit your order, you can choose to auto-renew your subscription at the end of its term, or let the subscription expire. You can cancel the auto-renew process. To cancel your subscription before it auto-renews, cancel the auto-renewal 30 days before the start of the next term.

You can configure monthly subscriptions to renew automatically each month. Weekly terms don't support automatic renewal.




Because orders are processed on a best-effort basis, ensure timely processing by placing orders as early as possible.

## Before you begin

Make a QIR with the selected option in the [quota list](https://docs.cloud.google.com/document-ai/quotas#quotas_list). You'll be contacted after the request is reviewed.

## Make a capacity reservation request

To make the request:

  1. In the Google Cloud console, go to the **IAM & Admin > Capacity Reservation** page: 

[Capacity Reservation](https://console.cloud.google.com/ai/document-ai/capacity-reservations/list)

  2. Near the page header, click squareadd **Create new capacity reservation**. This will take you to a two-page request form.

  3. Fill out the **Configure** page with the following:

     * Fill out a name for the order.
     * Select a region.
     * Select the processor version from the drop-down menu.
     * Write the number of additional pages per minute needed per month.
     * Select the monthly subscription term.
     * Select start date and time.
     * Select an auto-renew option from the drop-down.
  4. Click **Continue**.

  5. On the second page, you'll see an estimated cost per month. To validate the purchase, enter **Confirm**.

  6. Click **Confirm and submit**.




You can see the request status in the **Capacity Reservation** tab. The three possible statuses include:

  * **Inactive** : The subscription hasn't started yet.
  * **Active** : The subscription is ongoing.
  * **Completed** : The subscription has finished.



## What's next

For more information on available quotas, see the Document AI [Quota](https://docs.cloud.google.com/document-ai/quotas) page.

[ Previous arrow_back  Limits  ](https://docs.cloud.google.com/document-ai/limits)

[ Next Videos  arrow_forward  ](https://docs.cloud.google.com/document-ai/docs/videos)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
