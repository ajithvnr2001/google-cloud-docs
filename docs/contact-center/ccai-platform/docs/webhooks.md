---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/webhooks/
title: Webhooks for the chat API platform \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:03:33.510378+00:00
---

# Webhooks for the chat API platform  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/webhooks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Webhooks for the chat API platform Stay organized with collections  Save and categorize content based on your preferences. 

With webhooks, the apps API sends your application a real-time notification each time a relevant event occurs during a chat session—for example, when a chat is created, a message is received, or a chat is transferred or escalated. Use webhooks to react to chat activity as it happens instead of polling the API.

Webhooks are scoped to chat sessions on the apps API. Contact Center AI Platform delivers all supported apps API chat webhook events as HTTP `POST` requests to a single webhook URL that you configure. There's no per-event subscription.

## Before you begin

  * You must be an administrator (or have a role with permission to edit Developer Settings) to configure webhooks.
  * Prepare an endpoint that can receive HTTP `POST` requests. The webhook URL must use HTTPS.



## Turn on webhooks

When you turn on webhooks, Contact Center AI Platform delivers webhook events to your configured URL and the URL and secret fields appear. When webhooks are off, no events are sent.

To turn on webhooks, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.
  2. Go to the **Webhooks** pane, and then click the **Webhooks** toggle to the on position.



## Configure the webhook URL

  1. In **URL** , enter your webhook endpoint.
  2. Confirm the endpoint uses HTTPS and can receive `POST` requests. Contact Center AI Platform sends all supported events to this single URL.



## Generate signing secrets

Contact Center AI Platform signs every webhook request so your application can confirm the request came from Contact Center AI Platform. It sends the signature in the `X-Signature` request header, and the signing timestamp in `X-Signature-Timestamp`. You can configure up to two signing secrets:

  * **Primary secret** : The main token used to sign webhook requests.
  * **Secondary secret** : An optional second token. When a secondary secret is set, Contact Center AI Platform signs each request with both secrets, which lets you rotate secrets without missing events.



Generate each secret separately. To generate a secret, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.
  2. Go to the **Webhooks** pane.
  3. In the **Primary Secret** section, click **Generate**. Click **Copy** to copy a secret and store it securely. The full secret is shown only right after you generate it. Afterward it is masked.
  4. Optional: In the **Secondary Secret** section, click **Generate**. Click **Copy** to copy a secret and store it securely.
  5. Confirm in the warning dialog. A new secret takes effect immediately, so anything still using a replaced secret fails.



## Rotate signing secrets

When a primary secret exists, a **Rotate Secrets** action becomes available. Rotating your secrets periodically is a security best practice. Because Contact Center AI Platform signs each request with both the primary and secondary secrets, you can rotate without interrupting delivery:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.
  2. Make sure both a primary and a secondary secret are set.
  3. Click **Rotate Secrets** to swap the primary and secondary secrets.
  4. Update your application to verify signatures against the new active secret. During the overlap, Contact Center AI Platform signs each request with both configured secrets, so accept either one and delivery is not interrupted.



## Save your configuration

Select **Save** to apply the webhook's enabled state and URL. Generating or rotating a secret takes effect immediately and does not require a save operation. Contact Center AI Platform begins delivering events after webhooks are enabled and a webhook URL and primary secret are set.

## What your application receives

After you enable webhooks, Contact Center AI Platform sends an HTTP `POST` request for each supported chat event, such as lifecycle changes, participant activity, messages, transfers, escalations, web forms, and dismissal warnings. Each request body is a JSON envelope with `event_type`, `timestamp`, `chat_id`, and an event-specific `body`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
