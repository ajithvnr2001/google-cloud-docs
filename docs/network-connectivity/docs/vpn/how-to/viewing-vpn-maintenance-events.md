---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/viewing-vpn-maintenance-events/
title: Identify VPN maintenance events \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:45.199545+00:00
---

# Identify VPN maintenance events  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/viewing-vpn-maintenance-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Identify VPN maintenance events Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of Cloud VPN maintenance events and how you can identify them using log messages.

In the Google Cloud console, the following messages might appear: **Starting VPN Task maintenance** or **VPN task maintenance Completed**. These messages indicate that a Cloud VPN maintenance event occurred during a specific time period.

## View Cloud VPN maintenance events

You can view maintenance event logs by using the Google Cloud console.

###  Console 

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Select the **Cloud VPN Gateway** as Resource Type.

  3. In the **Logs** column, click **View**.

The default query appears in the query builder.

  4. From the default query, note the value of the tunnel ID of the `resource.labels.tunnel_id` variable.

  5. Build a new query by using the `resource.labels.tunnel_id` value from the previous query as follows:
         
         resource.labels.tunnel_id=TUNNEL_ID textPayload=~"Starting VPN
         Task maintenance" 

  6. Check the logs for the following messages:

     * **Starting VPN Task maintenance** : this message indicates the beginning of the maintenance process for a specific VPN task.

     * **VPN task maintenance Completed** : this message confirms that the maintenance for the VPN task has successfully finished.




These maintenance activities are designed to be non-disruptive, so that users have continuous service—no packet loss, service interruptions, or downtime during these events.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
