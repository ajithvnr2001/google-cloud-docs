---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/standard-reports-voicemail-details-data-set/
title: Standard Reports: Voicemail Details Dataset \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:42.466918+00:00
---

# Standard Reports: Voicemail Details Dataset  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/standard-reports-voicemail-details-data-set/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Standard Reports: Voicemail Details Dataset Stay organized with collections  Save and categorize content based on your preferences. 

CCAI Platform provides standard reports for agent and queue voicemails.

## Voicemail Details Report

The **Voicemail Details** report reflects the number of voicemails received. The report displays one line for each interaction that resulted in a voicemail being left by the customer.

This report includes the name of the queue, timestamps, the duration of the voicemail along with the URL link to the voicemail recording.

**IMPORTANT:** The term **read** is used throughout this report. Since the recordings are stored in the customer CRM, from a reporting perspective there is no way to acknowledge that a recording was listened to. In this report **read** means that an agent was **assigned**.

The **Voicemail Details** report can be found at **Reports > Queues**.

The metrics included in this report are as follows:

**Metric Name** | **Definition**  
---|---  
**Queue Name** | The name of the queue including the full path names if the queue is a sub queue - where the interaction came into. In this report - this is specifically where the **voicemail** function would be offered to the caller.  
**Language** | The language associated with the queue.  
**Agent Name** | The name of the Agent. In this report - this is specifically the Agent that read the voicemail.  
**Agent ID** | The ID of the Agent that read the voicemail.  
**Agent Email** | The email address of the Agent that read the voicemail.  
**Start Time stamp** | The timestamp of when the voicemail started being recorded. This formats as date and hh:mm:ss UTC timestamp.  
**VM Duration** | The length of time of the voicemail. This formats in seconds.  
**Deflected from Transfer** | Indicates whether the voicemail was a deflection after a transfer  
**Voicemail Received** | Indicates whether the voicemail was received. This formats as **True** or **False**. **Note:** If there is an error with the voicemail recording, the columns **Voicemail Received** and **Voicemail Read** will both display **FALSE**.  
**Voicemail Read** | Indicates whether the voicemail was read. This formats as **True** or **False**. **Note:** If there is an error with the voicemail recording, the columns **Voicemail Received** and **Voicemail Read** will both display **FALSE**.  
**URL Link** | The URL link to the voicemail recording. The recordings are stored in the Customer's CRM.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
