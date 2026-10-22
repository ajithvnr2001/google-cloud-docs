---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/overview/
title: Telephony integration overview \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:42:47.135275+00:00
---

# Telephony integration overview  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/overview/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Telephony integration overview Stay organized with collections  Save and categorize content based on your preferences. 

Send audio data to Conversational AI with a telephony-based integration by establishing telephony connectivity to Google's SIP endpoints, which are hosted by the Google Telephony Platform (GTP).

This document describes how to integrate your Session Border Control (SBC) system with the Google Telephony Platform (GTP) to make voice data available in Conversational Agents.

![Flowchart outlining telephony integration](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/integration.png)

## Integration process

The telephony integration process has two main components:

  * Set up your Conversational AI Google Cloud project.
  * Configure and validate your SBC.



### Conversational AI Google Cloud project setup

  * Define a Conversational AI Google Cloud project.
  * Complete the allowlist process for the Google Cloud project for Conversational AI SBC integration.
  * Configure Dialogflow, Conversational AI conversation profile, and phone number.
  * Optional: Request a quota increase for the Dialogflow CX Phone Gateway call length.
  * Optional: Enable audit logging for the Dialogflow API.



### SBC configuration and validation

  * Review supported SBC vendors and firmware versions.
  * Configure supported SBC signaling and media protocols.
  * Configure the SBC TLS settings.
  * Create a SIP trunk on GTP.
  * Review telephony connectivity network requirements.
  * Configure the SBC for a SIP connection to GTP.
  * Perform a SIP connectivity test with a SIP OPTIONS ping.
  * Configure SIP headers for Conversational AI conversations.
  * Perform test calls.
  * Review the Dialogflow conversation history.
  * Optional: Review the Google Cloud Logs Explorer.



## What's next

  * Learn how to [set up a Google Cloud project](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/cloud-setup) for the telephony integration.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
