---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-channel/
title: Overview and expected behavior \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:22.596964+00:00
---

# Overview and expected behavior  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-channel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Overview and expected behavior Stay organized with collections  Save and categorize content based on your preferences. 

The email support channel lets you set up, manage, and handle email support. The email channel receives support request emails from end-users and distributes them to support agents. This routing can be automated or manual.

**Note:** Email channel is only available for Salesforce, Zendesk, Kustomer, and Custom CRMs.

## Expected agent support behaviors

**In-Email** is a default system agent status and cannot be removed. This agent status is available only when **CCAIP Email Channel** is enabled, and the agent is assigned to at least one email queue. `In-Email` is not automatically set for the agent; they can manually set themselves to this status using the Agent Adapter for Email. Supervisors can also set this status for their agents using the Admin Portal.

Agents can receive incoming calls and chats when they are set to `In-Email` status. When an agent in `In-Email` status goes into a call or chat session the agent status will be overridden to either `In-Call` or `In-Chat` depending on which channel they're using.

## Expected CRM behaviors

A new CRM ticket will be created for:

  * New emails received in the email channel.
  * Emails sent out through the email channel.
  * New email replies received in the email channel on a previously existing email thread for which no CRM ticket link exists.
  * Emails sent using the email channel on a previously existing email thread for which no CRM ticket link exists.



If a thread already exists that is linked to a CRM case, the replies and subsequent messages will remain linked to the existing CRM ticket. A direct link to the latest email in the email thread will be generated and added as a comment to the linked CRM ticket when an email is sent or received.

A standard comment is attached to the linked CRM ticket when an email is sent or received for the first time containing the following elements:

  * Sent by: `{sender's email address}`
  * Received by: `{receiver's email address}`
  * Session ID: `{email session ID}`
  * Assigned agent: `{agent name}`
  * Queue: `{queue name}`
  * Subject: `{email subject}}`



Depending on your CRM ticket management configurations, the following elements might also appear:

  * A copy of the email contents in the thread posted (as a comment) in the linked CRM ticket.
  * A PDF copy of the email thread attached to the linked CRM ticket.



External storage locations (default and customizable path) are supported. These settings can be found in **Settings > Email**.

## Attachment restrictions

The following table outlines attachment restrictions for email channels. All attachments are virus scanned before being added.

Images allowed file types | Video allowed file types | Audio allowed file types | Documents allows all file types EXCEPT  
---|---|---|---  
JPEG/JPG, PNG, GIF, TIFF, RAW, WebP | MP4, MOV, AVI, WMV, WebM | MP3, WAV | EXE, DLL, BAT, ZIP, RAR, SCR, BIN  
  
## What's next

Learn how to [configure an email channel](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-channel-config) in your system.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
