---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-queue-status-endpoint/
title: The queue status endpoint \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:22.043973+00:00
---

# The queue status endpoint  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-queue-status-endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  The queue status endpoint Stay organized with collections  Save and categorize content based on your preferences. 

The queue status endpoint provides real-time data for leaf queues, including estimated wait times, agent availability, callback slot capacity, hours of operation, and holidays. This lets voice AI systems dynamically decide whether to escalate a call to a live agent or offer scheduled callback windows to the caller. For more information, see [Queue status](https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-queue-endpoints#queue-status).

## Queue status endpoint workflow

The queue status endpoint is exposed through the apps API and is designed to be called by trusted server-side applications such as voice AI platforms or orchestration services.

Here is the queue status endpoint workflow at a high level:

  1. Your app sends a request to the queue status endpoint with the following information:

     * One or more queue IDs.

     * A language code.

     * Optional callback window parameters, which determine how far into the future to calculate callback time slots.

  2. The request returns the following information:

     * Real-time queue metrics: Estimated wait time (EWT), calls in queue.

     * Agent metrics: Logged in, available, breakthrough.

     * Callback capacity estimation.

     * Queue configuration: Hours of operation (hoops), holidays.

  3. Your app uses the information to decide to do the following:

     * Route to a live agent if EWT and agent availability are acceptable.

     * Offer a callback and show the next available callback time slots.




## Use cases

Although the queue status endpoint doesn't directly modify CRM records, it is commonly used by voice AI systems or orchestration systems that integrate with external platforms such as Salesforce, Zendesk, or ServiceNow. This section describes some typical use cases.

### Real-time transfer decision

Here's a real-time transfer decision workflow:

  1. Your voice AI system calls `/apps/api/v1/queues/status` to get EWT and agent availability.

  2. If EWT is within an acceptable threshold and there are available agents, the voice AI system transfers the call to the queue.

  3. If EWT is too high or there are no available agents, the voice AI system instead offers a callback and uses the callback periods to present time options.




### Callback scheduling helper

Here's a callback scheduling helper workflow:

  1. Before presenting callback options, your system calls the queue status endpoint to get the following:

     * Valid callback slots

     * Hours of operation and holiday context

  2. Your application calls the relevant Apps API callback creation endpoints, using only the time slots that the queue status endpoint has confirmed as available.




### Holiday and after-hours behavior

When the queue status endpoint indicates that the queue is outside of hours of operation or on holiday, the voice AI system can do either of the following:

  * Offer only callbacks at valid future times.

  * Provide a tailored message—for example, "We're closed now, here are the next available callback times."




Any CRM-specific logic (for example, what to do if a ticket is closed, or whether to create or update a record before scheduling a callback) is handled in your integration or with other apps API capabilities. The role of the queue status endpoint is to supply the queue-side capacity and timing information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
