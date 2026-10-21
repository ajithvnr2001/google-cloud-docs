---
url: https://docs.cloud.google.com/agent-assist/docs/troubleshooting-api-services-usage-spike/
title: Troubleshooting API and services latency spike \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:27:44.815318+00:00
---

# Troubleshooting API and services latency spike  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-assist/docs/troubleshooting-api-services-usage-spike/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Troubleshooting API and services latency spike Stay organized with collections  Save and categorize content based on your preferences. 

This document gives an overview of the debugging process to understand the usage of **APIs and Services** in the Google Cloud console and also their latency spike.

First, follow these steps to identify conversation IDs with high latency:

  1. Open **[Google Cloud console](https://console.cloud.google.com)** and go to the **APIs & Services**.
  2. Click **Enabled APIs and Services**.
  3. Go to **Metrics** and select the **API method** under **Methods**. 



The latency traffic graph appears, labeled **Traffic by API method**.

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/aa-troubleshoot-screenshot1.png)

Next, ensure that you enable audit logging.

  1. Go to **Audit Logs**.
  2. Check the options **Admin Read** , **Data Read** and **Data Write**.
  3. Click **Save**.



![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/aa-troubleshoot-screenshot2.png)

Next, identify the conversation IDs with latency longer than a certain value in `Log analytics`. For example, in the following screenshot, you can see conversations longer than 10 seconds on a particular day. 

  1. Go to **Log analytics**.
  2. Provide the time against **TIMESTAMP_DIFF**.



![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/aa-troubleshoot-screenshot4.png)

Alternatively, use the timestamp to identify specific conversations during a certain period in `Log explorer`. 

  1. Enter the name of the method in **protoPayload.methodName**.
  2. Enter the time range in **Timestamp**. 
  3. View the results in **Log fields**.



![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/aa-troubleshoot-screenshot3.png)

You can access any Agent Assist APIs with Cloud Logging enabled by following all of the preceding steps.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
