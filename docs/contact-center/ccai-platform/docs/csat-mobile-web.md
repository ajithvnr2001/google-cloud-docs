---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/csat-mobile-web/
title: Mobile and web Customer Satisfaction Ratings (CSAT) \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:11.295292+00:00
---

# Mobile and web Customer Satisfaction Ratings (CSAT)  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/csat-mobile-web/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Mobile and web Customer Satisfaction Ratings (CSAT) Stay organized with collections  Save and categorize content based on your preferences. 

Customer Satisfaction Ratings, also known as CSAT are valuable indicators of support interaction effectiveness. CCAI Platform offers a straightforward CSAT option for customers with the Mobile or Web SDK.

**Note:** For the CSAT prompt to appear, both the agent and the consumer must have sent at least one message.

## CSAT details

  * Available for inbound sessions only.

  * CSAT is based on a 1-5 star rating.

  * Consumers are not able to skip the rating screen when enabled.

  * When enabled, CSAT UI will show for web and mobile SDKs.

  * To set a time limit for how long a consumer has to rate the interaction, please reach out to Support.




### Admin Configuration

  1. In the CCAI Platform portal, go to **Settings** > **Operation Management**.

  2. To enable the CSAT UI in your SDK, navigate to the Customer Satisfaction Rating section and click to toggle **On**.

  3. **Post CSAT in CRM ticket** to attach the numerical customer rating to the CRM record.

  4. Mark the checkbox next to **enable Qualitative Feedback** to allow end-users to provide feedback in an open-text field. All Qualitative feedback will be added to the CRM record. _Feedback text limit is 3000 characters._

  5. Click **Set CSAT** to save.




## Mobile and Web UI

The user interface for mobile and web experience are outlined in the following sections.

### Mobile

After the voice or chat interaction, the consumer will be taken to a screen similar to the one in the Mobile SDK.

### Web

After the voice or chat interaction, the consumer will be taken to a screen similar to the one in the Web SDK.

## Viewing CSAT results

Scores are stored in CCAI Platform dashboards and reports, as well as in your CRM. **Comments will not be stored in CCAI Platform, they will be stored in your CRM as long as the setting has been enabled** as shown previously.

### Dashboards

  1. In the CCAI Platform portal, go to **Dashboards** > **Call** OR **Chat.**

  2. Go to the **CSAT** section. This shows the average CSAT for the time duration selected in the dashboard filters.




### CRM

Depending on which CRM you use and your specific configuration, CSAT ratings are stored in the comments or Case details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
