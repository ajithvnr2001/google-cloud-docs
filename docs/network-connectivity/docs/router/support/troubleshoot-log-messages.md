---
url: https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-log-messages/
title: Troubleshoot Cloud Router log messages \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:18:15.542150+00:00
---

# Troubleshoot Cloud Router log messages  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-log-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot Cloud Router log messages

This guide is for troubleshooting log messages that appear in Cloud Router logs.

For additional troubleshooting information, see the following:

  * [Troubleshoot BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-sessions)
  * [Troubleshoot BGP peering](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-peering)
  * [Troubleshoot BGP routes and route selection](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-routes)



## `NOTIFICATION_RECEIVED` message appears in Cloud Router logs

A `NOTIFICATION_RECEIVED` message appears in the Cloud Router logs when the Cloud Router has received a `NOTIFICATION` message from the BGP peer. The `NOTIFICATION` message is a signal to Cloud Router that it should stop the BGP session.

When the Cloud Router receives a `NOTIFICATION` message from its BGP peer, Cloud Router closes the BGP connection with that peer and removes all its learned routes.

The BGP peer can send `NOTIFICATION` messages for a variety of reasons. For example, the peer might send a "Hold Timer Expired" message.

## `CONFIG_DISABLED` message appears in Cloud Router logs

A `CONFIG_DISABLED` message indicates that Cloud Router has intentionally stopped the BGP session. By stopping the BGP session, Cloud Router is attempting to immediately communicate an error state to its peer.

This message can appear due to any of the following reasons:

  * A user has disabled the BGP session by using the Cloud Router API, Google Cloud console, or the Google Cloud CLI. See [Disabling or removing BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/disabling-removing-bgp).

  * For a BGP session set up for Cloud VPN, the VPN tunnel associated with the BGP session has not established an IKE and child security association (SA). To troubleshoot VPN connectivity, see [Cloud VPN troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).

  * For a BGP session set up for Cloud Interconnect, the VLAN attachment is not configured or is in an admin-down state. To troubleshoot the issue further, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting) in the Cloud Interconnect documentation.

  * For a BFD-enabled BGP session, the BFD control detection timer on the Cloud Router has expired. When this occurs, the BGP session is stopped. For more information on BFD session states, see [BFD diagnostic messages and session states](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd-states).




## `LINK_DOWN` message appears in Cloud Router logs

A `LINK_DOWN` message appears in the Cloud Router logs when the link between the Google peering edge router and your VLAN attachment for Cloud Interconnect is down. The peering edge router is networking equipment that is managed by Google inside the colocation facility where you have provisioned your Cloud Interconnect connection.

The `LINK_DOWN` message is a signal that the corresponding BGP peer status is down. This message applies only to Cloud Interconnect-based BGP sessions.

## Route quota events appear in Cloud Router logs

A `WARNING` or `ERROR` event for `route_quota_events` indicates that a VPC network is approaching or exceeding its dynamic route quotas (`CLOUD-ROUTER-PREFIXES-FROM-OWN-REGION-Per-Region-Per-VPC` or `CLOUD-ROUTER-PREFIXES-FROM-OTHER-REGIONS-Per-Region-Per-VPC`).

If you see these logs, inspect the `affectedResource` field to identify which routes are being dropped. If you require more routes than the current limit allows, you can [request a quota increase](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#requesting-additional-quota).

## What's next

  * For more information about how to use Cloud Logging to monitor Cloud Router, see [View logs and metrics](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-logs-metrics).

  * For additional support, see [Getting support](https://docs.cloud.google.com/network-connectivity/docs/router/support/getting-support).

  * For information about BGP session states, see [BGP session states](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-states).

  * For information about diagnostic messages and session states related to Bidirectional Forwarding Detection (BFD), see [BFD diagnostic messages and session states](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd-states).

  * For issues related to using Cloud Router with Router appliance, see [Troubleshooting Router appliance](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting#troubleshooting-ra) in the Network Connectivity Center documentation.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
