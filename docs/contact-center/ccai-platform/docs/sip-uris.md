---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sip-uris/
title: SIP URIs \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:35.505571+00:00
---

# SIP URIs  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sip-uris/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  SIP URIs Stay organized with collections  Save and categorize content based on your preferences. 

A Session Initiation Protocol Uniform Resource Identifier (SIP URI) destination refers to a specific address or endpoint that can receive SIP-based communication. SIP is a protocol used for initiating, modifying, and terminating real-time communication sessions such as voice and video calls over IP networks. For more information about session types, see the [session type terminology](https://docs.cloud.google.com/contact-center/ccai-platform/docs/session-type-terminology) documentation.

With as [contact list](https://docs.cloud.google.com/contact-center/ccai-platform/docs/contact-list) you can create and save a list of SIP URIs, which are used to identify endpoints in a SIP-based communication network, such as VoIP (Voice over IP) systems. You can customize call routing and management in a communication system, depending on the specific needs and requirements of the organization.

SIP call transfers can be used to route incoming calls to appropriate destinations based on IVR menu selections or queue routing rules. For example, a consumer calling your support line may select an option in the IVR menu to be transferred to a specific department or agent based on their inquiry.

## Use cases

**Call overflow** : SIP call transfers can be used to manage call overflow situations where a queue becomes too busy or reaches its maximum capacity. Calls can be automatically transferred to alternative destinations, such as other queues or backup agents, to ensure efficient call handling and prevent call abandonment.

**Call distribution** : SIP call transfers can be used to distribute calls evenly or according to specific routing rules among agents or departments. This can help balance the workload and ensure fair distribution of calls, optimizing call handling efficiency and improving consumer service.

**Call consolidation** : SIP call transfers can be used to consolidate calls from multiple sources or channels into a single destination. For example, calls from different IVR menus or queues can be transferred to a centralized agent or department for unified handling and streamlined call management.

## Configure call transfers at the queue level

You can configure how calls are transferred to a contact in an IVR queue.

To configure call transfers at the queue level, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Queue**.

  2. In the **IVR (Interactive Voice Response)** pane, click **Edit / View**.

  3. Click the queue that you want to edit. 

  4. Go to **Automatic Redirection** and click the toggle to the show position.

  5. Select **Phone number or Outbound SIP transfer**.

  6. Do one of the following:

     * Select **Select from contact list**. Use the fields that appear to select a contact list and a destination.

     * Select **Enter phone number**. Enter a phone number in the field that appears.

     * Select **Enter SIP URI address**. Enter a SIP URI in the field that appears. Optionally select **Redirect using SIP REFER when available**.

**Note:** SIP REFER is only available when using [Bring-Your-Own-Carrier (BYOC)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/byoc).
  7. Click **Save Redirection**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
