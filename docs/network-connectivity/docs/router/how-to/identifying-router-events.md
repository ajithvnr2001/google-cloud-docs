---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/identifying-router-events/
title: Identify router maintenance events \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:04.295367+00:00
---

# Identify router maintenance events  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/identifying-router-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Identify router maintenance events

You can identify Cloud Router maintenance events and verify connectivity. For more information about maintenance events, see [Software maintenance](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/how-cloud-router-works#maintenance).

## Identify events using the _maintenance of router task_ message

In the Google Cloud console, the following message appears: **Maintenance of router task: BGP sessions will restart. Routes are preserved for the duration of the configured timers. These are normal events, and no data loss is expected to occur.**

This message indicates that a Cloud Router maintenance event occurred during the issue or time period.

## Identify events using a log-based metric

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. Find the Cloud Router from the list of Cloud Routers.

  3. In the **Logs** column, click **View**.

The default query appears in the query builder.

  4. From the default query, note the value of the router ID of the `resource.labels.router_id` variable.

  5. Build a new query by using the `resource.labels.router_id` value from the previous query as follows:
         
         resource.labels.router_id=ROUTER_ID
         textPayload=~"Maintenance of router task: BGP sessions will restart."
         

  6. Create an alert with a notification of a maintenance event by using the previous query.

This notification appears the first time the router is created and subsequently during every maintenance event.

For more information about creating an alert, see [Create an alert policy on a counter metric](https://docs.cloud.google.com/logging/docs/logs-based-metrics/charts-and-alerts#alert-on-lbm).




## Verify connectivity between the on-premises router and the Cloud Router

Use the following methods to verify connectivity:

  * For Cloud Router used with Cloud VPN, set up a dashboard for `network/received_packets_count` and `network/sent_packets_count` to monitor any loss in connectivity. For more information, see [View VPN metrics](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/viewing-logs-metrics#metrics).

  * For Cloud Router used with Cloud Interconnect, set up a dashboard for `network/attachment/sent_packets_count` and `network/attachment/received_packets_count` to monitor the connectivity of VLAN attachments. For more information, see [Interconnect metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#gcp-interconnect).




During Cloud Router maintenance events, metrics for each resource aren't expected to show any gap of connectivity.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
