---
url: https://docs.cloud.google.com/monitoring/alerts/sms-opt-out/
title: Opt out of SMS notifications \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:19.140395+00:00
---

# Opt out of SMS notifications  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/alerts/sms-opt-out/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Opt out of SMS notifications Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can use a text message to opt out of receiving notifications sent by using SMS notification channels. You can also use text messages to request information about how to opt out.

You can send text messages in English or in French, as required for compliance with US and Canadian regulations.

## Opt out of SMS-based notification

To opt out of SMS notifications, send one of the following messages as a reply to the SMS notification:

  * English: **STOP**
  * French: **ARRET**



Cloud Monitoring disables all notification channels associated with the phone number, **across all Google Cloud projects** , and sends a confirmation SMS message.

## Request opt-out information

To request information about how to opt out of SMS notifications, send one of the following messages as a response to the SMS notification:

  * English: **HELP**
  * French: **AIDE** or **INFO**



## Opt in to SMS-based notification

When you send a text message to opt out of receiving SMS notifications, then the affected channels are disabled. To start receiving SMS notifications again, edit the disabled notification channels to enable them. For information about editing notification channels, see the following:

  * [Use the Google Cloud console](https://docs.cloud.google.com/monitoring/support/notification-options#edit-delete-channel)
  * [Use the API](https://docs.cloud.google.com/monitoring/alerts/using-channels-api#api-update-channels)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
