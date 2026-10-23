---
url: https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/manage-alerts/
title: Manage alerts \u00a0|\u00a0 Network Intelligence Center - Performance Dashboard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:06.152121+00:00
---

# Manage alerts  |  Network Intelligence Center - Performance Dashboard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/manage-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Performance Dashboard ](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/using-performance-dashboard)



Send feedback 

#  Manage alerts Stay organized with collections  Save and categorize content based on your preferences. 

You can create alerts for high packet loss based on predefined conditions. The alerting policy for packet loss is triggered when the packet loss exceeds 5% for 5 minutes for any region pair. You can modify the alerting policy or create new alerting policies. For more information about creating and managing alerting policies, see [Introduction to alerting](https://docs.cloud.google.com/monitoring/alerts).

To create an alert and configure notifications, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Performance Dashboard** page. 

[Go to Performance Dashboard](https://console.cloud.google.com/net-intelligence/performance/dashboard/packet-loss)

  2. On the **Packet loss** tab, click **Create alert**. The **Alert policy templates** sidebar appears. 
  3. Select an alert policy template from the list or customize a configuration: 
     1. Select **High packet loss alert policy**. This policy triggers an alert when the packet loss exceeds 5% for 5 minutes for any region pair.
     2. To customize the alert policy, click **View options**.
     3. To edit the MQL alert template, click **Customize Alert Policy**.
  4. Configure notifications:

     1. Click **Use notification channel**. You can send your Google Cloud alerting data to your notification channel. The data sent to the channel recipients might contain sensitive information.

**Note:** Review your regulatory practices before you create the notification channel.
     2. In **Notification channels** , select the channel. Select where to receive notifications when incidents are triggered.

     3. To view existing channels and add more channels, in **Notification channels** , click **Manage Notification Channels**. For more information, see [Introduction to alerting](https://docs.cloud.google.com/monitoring/alerts).




## What's next

  * [Performance Dashboard metrics](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/viewing-perf-dash-metrics)
  * [Troubleshoot Performance Dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/support/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
