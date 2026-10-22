---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/priority-sgements/
title: Priority user segments \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:40.944266+00:00
---

# Priority user segments  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/priority-sgements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Priority user segments Stay organized with collections  Save and categorize content based on your preferences. 

Priority user segments are a way to give VIP and other high-value contacts the prompt, efficient service they expect by placing them at the front of the queue. When a consumer initiates a call or chat session, CCAI Platform checks for a contact record in the CRM. If the contact is marked as a Priority User, the consumer goes to the top of any queue they select.

## Feature details

When a call or chat session is initiated, CCAI Platform searches for a matching contact record in your CRM. If a match exists, the contact record is scanned for CRM fields. If the specified field matches a priority user segment, the session becomes high priority and jumps toward the front of the queue. The consumer is offered the same queue options as any other consumer, but no matter which one they chose, their session will be marked high priority.

### Other feature specifics

  * Once a priority segment is set up, contacts will be routed when reaching out from any entry point or channel:

    * IVR, Mobile SDKs and Web SDKs

    * Call, chat, and SMS

  * Applies no matter what queue is selected

  * Works in combination with queue priority and Direct Access Points




### Example use cases

  * Assign a VIP field that can be marked when a specific contact requires special treatment

  * Use a "stage" field and whenever a customer is in "Onboarding" they will be routed using priority segmentation

  * Use the "customer segment" field in your CRM and assign priority segmentation to "platinum" account contacts




## CRM configuration

The first step is to create a custom field in your CRM. Check your CRM specific documentation on how to create a custom field in your CRM

## Admin Config

From the CCAI Platform portal, use an administrator login to complete these steps:

  1. Allow CRM access for user segment information.

  2. Add a priority user segment.




### Allowing CRM Access for user segment information

  1. In the CCAI Platform portal, go to **Settings** > **Operation Management**.

  2. Under **CRM Access,** mark the checkbox to allow CCAI Platform to access the user segment information in your CRM.

  3. Click **Set General** to save.




### Adding a priority user segment

  1. In the CCAI Platform portal, go to **Settings** > **Operation Management** > **Priority User Segments**.

  2. Click **Add a user segment**.

  3. Click into the CRM Field and select from the available **CRM Fields.** Selection options should include any that have been created in your CRM (this is called the key in your CRM).

  4. Enter the user segment **CRM value** created in your CRM. If the selected value is "gold," when the field in your CRM shows "gold" on the contact record, the caller will be prioritized over other callers in the same queue.

  5. Click **Add** to save the priority user segment.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
