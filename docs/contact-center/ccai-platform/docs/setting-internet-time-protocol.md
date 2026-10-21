---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/setting-internet-time-protocol/
title: Setting Internet Time Protocol \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:49:45.831436+00:00
---

# Setting Internet Time Protocol  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/setting-internet-time-protocol/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Setting Internet Time Protocol Stay organized with collections  Save and categorize content based on your preferences. 

The time and date settings on an Agent's computer can greatly impact apps and services used throughout the day. For Contact Center AI Platform (CCAI Platform), if the settings are not set automatically by an internet service, time sync within the product can be off. This may present itself in the Agent Adapter where the agent status timer doesn't start at 0:00 when the status is changed. To resolve this issue, follow these steps:

## NTP server configuration with macOS

  1. From your system preferences, click **Date & Time.**

  2. Click the lock to unlock the ability to make changes.

![Mac lock icon](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fb649371f.png)

  3. When unlocked, replace the Apple address with the NTP server address `time.google.com`.

![Mac NPT address](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fb64c17d5.png)

  4. Exit System Preferences.




## NTP configuration for Microsoft Windows 10

  1. Go to your Windows Control Panel and find the **Date and Time** option.

  2. Click the **Internet Time** tab.

  3. Click **Change settings**.

![Windows change settings](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fb64f2e2e.png)

  4. Select **Synchronize with an Internet Time server**.

  5. Enter the NTP server: `time.google.com`.

  6. Click **Update now**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
