---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/verint/
title: Verint integration \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:52.195930+00:00
---

# Verint integration  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/verint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Verint integration Stay organized with collections  Save and categorize content based on your preferences. 

This feature provides an out-of-the-box integration with Verint's Face-to-Face Voice Interaction Recording solution. Data flow between Contact Center AI Platform (CCAI Platform) and Verint is automatically established and call recordings are pushed to the Verint server for single administration.

The Face-to-Face Voice Interaction Recording feature provides extended benefits when used in combination with other functionality in the Verint Workforce Optimization suite.

Benefits from features like:

  * Quality monitoring

  * Speech analytics

  * Desktop and process analysis

  * Performance management




When enabled, the CCAI Platform agent call adapter interacts with a Verint app on the agent's Windows device. The call adapter sends appropriate session metadata and the appropriate signals (start, pause, resume, stop recording) to the Verint app to manage call recording on the agent's device.

**Requirements**

  * Agent devices must run Windows OS

  * IT team needs to configure the Verint Face-to-Face Voice Interaction Recording app (msi) to each agents' Windows installation

  * Please contact your Customer Success Manager to activate this feature




## Set up Verint Face-to-Face recordings

When you specify an agent's email domain during setup, subsequent calls made that agent are recorded.

To set up Verint Face-to-Face recordings, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Session Data Export** pane, and then click **Manage Data Export Settings**. The **Session Data Export** page appears.

  3. Go to the **Verint Face-to-Face Recordings** pane and click the toggle to the on position.

  4. In the **Agent email domains** field, enter a space-separated list of email domains for the agents whose calls you want to record.

  5. Click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
