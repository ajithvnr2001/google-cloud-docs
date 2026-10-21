---
url: https://docs.cloud.google.com/agent-assist/docs/twilio-siprec/
title: Twilio SIPREC integration \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:06:05.183339+00:00
---

# Twilio SIPREC integration  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-assist/docs/twilio-siprec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Twilio SIPREC integration Stay organized with collections  Save and categorize content based on your preferences. 

You can integrate Twilio's SIPREC configuration with Google Cloud's Agent Assist. This integration allows Agent Assist to analyze Twilio's audio data.

## The architecture

Google Cloud CCAI acts as the [session initiation protocol (SIP)](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/siprec) recording server (SRS) and Twilio is the SIP recording client (SRC). Twilio has edge locations in Oregon and Virginia, and the Oregon location has Edge servers with a complete, fully qualified domain name that has been configured to communicate with CCAI. Using Twilio's generic [SIP recording (SIPREC)](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/siprec) connector, you can transmit traffic from the Oregon location to CCAI.

The following image illustrates how the Twilio SIPREC connector transmits voice data from the Twilio telephony SRC to the Google Cloud CCAI SRS.

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/twilio-siprec.png)

As part of CCAI, Agent Assist can then send transcripts of that voice data with suggestions back to the Twilio agent desktop using Cloud Run, Pub/Sub, and Memorystore for Redis.

## Configure SRS details at Twilio SIPREC connector

Follow these steps to access a Twilio SIPREC connector:

  1. Visit the Twilio [Stream Connectors Console page](https://www.twilio.com/console/voice/stream-connectors).
  2. Select **SIPREC Connector**.
  3. Give your connector a unique name.



For the SRS, use the following connection string and replace the phone number with the phone associated with your conversation profile. The phone number should be formatted as +1XXXXXXXXXX.
    
    
    sip:<<enter_phone_number_here>>@216.239.36.145:5672;transport=tls;secure=true;edge=umatilla

For more details, see [Twilio's SIPREC documentation](https://www.twilio.com/docs/voice/api/siprec).

## Configure Twilio Studio

Follow these steps to configure Twilio Studio for SIPREC integration:

  1. Navigate to Twilio Studio and select the flow associated with the phone that your customers use to dial your contact center.
  2. Add a new plugin from the widget library called Fork Stream.
  3. Connect the incoming call trigger to the Fork Stream widget and the next connection to the rest of your flow.
  4. Configure the widget with the following information:

     * **Widget Name** : A unique name for your widget
     * **Stream Action** : Start
     * **Stream Name** : A unique name for your stream
     * **Stream Type** : SIPREC
     * **Connector Name** : The name of the connector you created in the previous section
     * **Tracks** : Both Tracks
     * **Stream Parameters** : 
       * Key: conversation
       * Value: `projects/<<gcp-project-id>>/conversations/{trigger.call.CallSid}`



For more information, read about [Twilio's Fork Stream widget](https://www.twilio.com/docs/studio/widget-library/fork-stream).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
