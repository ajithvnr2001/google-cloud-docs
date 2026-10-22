---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/siprec/
title: Audio conversation data \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:51.723716+00:00
---

# Audio conversation data  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/siprec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Audio conversation data Stay organized with collections  Save and categorize content based on your preferences. 

Customer Experience Insights supports the use of audio conversation data in addition to chat conversation data. This is facilitated through a **SIPREC endpoint** , a protocol that you can use to establish recording sessions and report metadata. SIPREC is a private GA feature compatible with all CCAI products.

SIPREC works in combination with [Cloud Speech-to-Text](https://docs.cloud.google.com/speech-to-text/docs) to generate transcripts of your audio data before it can be analyzed by CX Insights. SIPREC can also be used in combination with [Agent Assist](https://docs.cloud.google.com/agent-assist/docs) (to provide agent suggestions) and [Cloud Storage](https://docs.cloud.google.com/storage/docs) (to store audio data and transcripts) depending on your business needs.

## SIPREC overview

The SIPREC protocol is used between a Session Recording Client (SRC) and a Session Recording Server (SRS).

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/insights/images/siprec1.png)

An SIP user agent acts as the source of the recorded metadata & media, sending it to the recording service endpoint. The SRC could be a personal device (for example, SIP phone), application server, media server, an SIP media gateway (MG), or a Session Border Controller (SBC).

SBC and PBX phone systems are common SRCs in many call centers. There are many different SBC and PBX systems on the market that support SIPREC. Some popular examples are listed, and many additional systems are also compatible.

  * SBCs: Cisco Cube, Avaya SBCE, Oracle E-SBC, Sonus SBC, Genband SBC, MetaSwitch Perimeta.
  * PBX systems: Broadworks, Metaswitch.



Each SRC solution sends the metadata contained in the SIP header (caller ID, extension number, and so on). Different manufacturers choose different types of metadata to send.

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/insights/images/siprec2.png)

## Implement SIPREC

SIPREC integration usually must be custom-designed for each customer, and thus is a lengthy process that can take up to several months. If you are interested in implementing this feature, contact your Google representative.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
