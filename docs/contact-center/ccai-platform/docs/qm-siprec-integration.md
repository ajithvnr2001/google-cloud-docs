---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/qm-siprec-integration/
title: QM and SIPREC integration \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:36.317384+00:00
---

# QM and SIPREC integration  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/qm-siprec-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  QM and SIPREC integration Stay organized with collections  Save and categorize content based on your preferences. 

With Contact Center AI Platform (CCAI Platform), you can export session data directly to your quality management (QM) application or session initiation protocol real-time event collection (SIPREC) application.

## Application types

This section shows the types of applications that can accept session data exports from CCAI Platform.

### QM

You can export call or chat events to your QM application. For QM integration, you need a QM application that can ingest computer technology integration (CTI) events. For information about the call and chat events that CCAI Platform exports for QM integration, see the following:

  * [QM call session data](https://docs.cloud.google.com/contact-center/ccai-platform/docs/qm-call-session-data)

  * [QM chat session data](https://docs.cloud.google.com/contact-center/ccai-platform/docs/qm-chat-session-data)




### SIPREC

You can export call events to your SIPREC application. Google recommends setting up a SIPREC stream to receive SIPREC call events.

## Compare QM call events with SIPREC call events

QM and SIPREC call events are used for different purposes, so which option you choose depends on your use case. The following table outlines their main differences.

| QM call events | SIPREC call events  
---|---|---  
**Purpose** | Quality management and call monitoring. Typically used for activities like call recording, evaluating agent performance, and ensuring compliance with quality standards. | Real-time event collection and recording of SIP (Session Initiation Protocol) communications. SIPREC is a protocol used for recording voice and video calls in real-time or near real-time, often used for compliance, security, and troubleshooting purposes.  
**Use cases** | Crucial for industries where regulatory compliance and quality control are important, such as contact centers, financial institutions, and healthcare organizations. Often used for monitoring customer interactions and assessing agent performance. | Typically used in scenarios where it's necessary to record and capture SIP-based communication sessions, such as VoIP (Voice over Internet Protocol) calls. Important in industries where regulatory compliance, legal requirements, or security monitoring are priorities.  
**Content** | Call recordings, call metadata (such as call start and end times), and associated data relevant to quality assessments. | Information related to the setup and teardown of SIP sessions, as well as the media streams (audio and video) being exchanged during the session.  
  
## Export session events to your QM application

To export session events to your QM application, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Session Data Export** pane, and then click **Manage Data Export Settings**. The **Session Data Export** page appears.

  3. Click the **QM Integration** toggle to the on position.

  4. To export call events to your QM application, do the following:

     1. Select the **QM Call Events - send call sessions events** checkbox.

     2. In the **API Endpoint** field, enter the endpoint for your QM application.

     3. In the **Username** field, enter a username to authenticate with your QM application.

     4. In the **Password** field, enter a password to authenticate with your QM application.

  5. To export chat events to your QM application, do the following:

     1. Select the **QM Chat Events - send chat sessions events** checkbox.

     2. In the **API Endpoint** field, enter the endpoint for your QM application.

     3. In the **Username** field, enter a username to authenticate with your QM application.

     4. In the **Password** field, enter a password to authenticate with your QM application.

  6. Click **Save**.




## Export call events to your SIPREC application

To export call events to your SIPREC application, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Session Data Export** pane, and then click **Manage Data Export Settings**. The **Session Data Export** page appears.

  3. Click the **QM Integration** toggle to the on position.

  4. Select the **SIPREC Call Events - send call sessions events** checkbox.

  5. In the **API Endpoint** field, enter the endpoint for your SIPREC application.

  6. In the **Username** field, enter a username to authenticate with your SIPREC application.

  7. In the **Password** field, enter a password to authenticate with your SIPREC application.

  8. Click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
