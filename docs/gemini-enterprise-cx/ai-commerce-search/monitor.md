---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/monitor/
title: Set up Cloud Monitoring alerts \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:47.101589+00:00
---

# Set up Cloud Monitoring alerts  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/monitor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Set up Cloud Monitoring alerts Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can create alerts for AI Commerce Search, including examples of creating alerts for user event recording, predictions, and searches.

For information about data quality alerts, see [Data quality alerts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/data-quality#data-quality-alert).

For information about troubleshooting errors and viewing error logs, see [Troubleshooting data upload issues](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/error-reporting).

## Introduction

Keeping your catalog up to date and recording user events successfully is important for getting high-quality results. Even if your initial imports and event recording are successful, monitoring error rates is still needed in case of unexpected environmental issues, such as network connectivity failures.

You should set up Cloud Monitoring alerts so you can take action promptly in case any issues arise with user event recording, predictions, and search results. You can also monitor recent data integration error rates in the Google Cloud console at any time.

## Set up Cloud Monitoring alerts

Cloud Monitoring can be set up to alert on a large number of triggers. When you set up alerts, AI Commerce Search suggests several to set up. If you're unsure which alerts to set up, start with setting up alerts for prediction errors, search errors, and reductions in user event recording.

### Set up an alert for prediction errors

Generally, calling the `predict` method should rarely return an error. This alert is triggered if the number of errors returned by the predict method causes the error ratio to stay above the given threshold for more than 5 minutes. You can adjust the threshold to suit your environment.

To set up alerts from the AI Commerce Search in Gemini Enterprise for Customer Experience console:

  1. Go to the **Monitoring** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Monitoring page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/monitoring/)

  2. Click _add_**Recommended Alerts**.

The Recommended Alert Policies panel appears on the right. It displays a list of recommended alerts to set up for your project.

  3. Enable **High predict error ratio**.

  4. Optionally, adjust the threshold to suit your environment.

The default predict error ratio is 0.03.

  5. Choose a notification channel through which you'll be notified if the alert is triggered, such as an email address or mobile device.

To set up a new notification channel, select **Notification Channels > _refresh_ Manage Notification Channels**. See [the Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/support/notification-options) for more about creating and editing channels.

  6. Click the **Submit** button to create your alert.




You can also create a custom alert by using Cloud Monitoring. For more information, see [the Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/alerts).

### Set up an alert for search errors

This alert is triggered if the number of errors returned by the `search` method causes the error ratio to stay above the given threshold for more than 5 minutes. You can adjust the threshold to suit your environment.

To set up alerts from the AI Commerce Search in Gemini Enterprise for Customer Experience console:

  1. Go to the **Monitoring** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Monitoring page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/monitoring/)

  2. Click _add_**Recommended Alerts**.

The Recommended Alert Policies panel appears on the right. It displays a list of recommended alerts to set up for your project.

  3. Enable **High search error ratio**.

  4. Optionally, adjust the threshold to suit your environment.

The default threshold ratio is 0.03.

  5. Choose a notification channel through which you'll be notified if the alert is triggered, such as an email address or mobile device.

To set up a new notification channel, select **Notification Channels > _refresh_ Manage Notification Channels**. See [the Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/support/notification-options) for more about creating and editing channels.

  6. Click the **Submit** button to create your alert.




You can also create a custom alert by using Cloud Monitoring. For more information, see [the Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/alerts).

### Set up an alert for user event recording reduction

If you see a drop in user event recording that lasts for a prolonged period of time, there could be issues with your user event recording code. This alert is triggered if you don't record any user events for 10 minutes.

To set up a user event recording reduction alert from the AI Commerce Search in Gemini Enterprise for Customer Experience console:

  1. Go to the **Monitoring** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Monitoring page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/monitoring/)

  2. Click _add_**Recommended Alerts**.

The Recommended Alert Policies panel appears on the right. It displays a list of recommended alerts to set up for your project.

  3. Enable **User events record reduction**.

  4. Choose a notification channel through which you'll be notified if the alert is triggered, such as an email address or mobile device.

To set up a new notification channel, select **Notification Channels > _refresh_ Manage Notification Channels**. See [the Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/support/notification-options) for more about creating and editing channels.

  5. Click the **Submit** button to create your alert.




If you are using a method other than [`WriteUserEvent`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#writeusereventrequest), such as [`ImportUserEvents`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#importusereventsrequest), you can also create a custom alert by using Cloud Monitoring. For more information, see the [Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/alerts).

### Set up an alert for unjoined user events

This alert is triggered if the ratio of user events that aren't associated with valid products stays above the given threshold for more than one or twelve hours. You can choose the time window and adjust the threshold.

To set up a user event recording reduction alert from the AI Commerce Search in Gemini Enterprise for Customer Experience console:

  1. Go to the **Monitoring** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Monitoring page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/monitoring/)

  2. Click _add_**Recommended Alerts**.

The Recommended Alert Policies panel appears on the right. It displays a list of recommended alerts to set up for your project.

  3. Enable **Ratio of unjoined user events ratio is above the threshold for last hour** or **Ratio of unjoined user events increases above threshold for last 12 hours**.

  4. Optionally, adjust the threshold to suit your environment.

The default unjoined events ratio is 0.1. This means that if more than 10% of total events ingested are not joined with a valid product within the specified time window, an alert is triggered.

  5. Choose a notification channel through which you'll be notified if the alert is triggered, such as an email address or mobile device.

To set up a new notification channel, select **Notification Channels > _refresh_ Manage Notification Channels**. See [the Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/support/notification-options) for more about creating and editing channels.

  6. Click the **Submit** button to create your alert.




## What's next

  * [Troubleshoot your errors using Error Reporting](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/error-reporting).
  * Learn more about [Google Cloud Observability alerting](https://docs.cloud.google.com/monitoring/alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
