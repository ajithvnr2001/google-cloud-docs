---
url: https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-sessions/
title: Troubleshoot BGP sessions \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:10.829468+00:00
---

# Troubleshoot BGP sessions  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-sessions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot BGP sessions

This guide is for troubleshooting BGP sessions, such as BGP sessions that fail to establish and BGP resets.

For additional troubleshooting information, see the following:

  * [Troubleshoot BGP peering](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-peering)
  * [Troubleshoot BGP routes and route selection](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-routes)
  * [Troubleshoot Cloud Router log messages](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-log-messages)



## BGP session failed to establish

Check that the settings on your on-premises BGP router and the settings on your Cloud Router are correct. For detailed information, view the Cloud Router [logs](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-logs-metrics).

If you're creating a Cloud VPN tunnel, check that the [status of the tunnel](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details) is `ESTABLISHED`. If it isn't, to troubleshoot the issue, see [Cloud VPN troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).

## IPv4 and IPv6 addresses for BGP sessions

Support for IPv6 BGP sessions is in [Preview](https://cloud.google.com/products#product-launch-stages).

The IPv4 and IPv6 addresses that you can use for a BGP session depend on the product you use. For complete details, see [BGP peering addresses](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bgp#bgp-peering-addresses).

## Invalid value for the field `resource.bgp.asn`

You may get the following error:

_"Invalid value for field`resource.bgp.asn`: `######`. Local ASN conflicts with peer ASN specified by a router in the same region and network."_

The Cloud Router is attempting to establish a BGP session with an on-premises device that has the same ASN as the Cloud Router. To resolve this issue, change the ASN of your device or Cloud Router.

## IPv6 BGP session fails to establish

If you are experiencing difficulty establishing a connection with your IPv6 BGP peer, do the following:

  1. Verify that the corresponding VLAN attachment or HA VPN tunnel is connected.

  2. Verify that the VLAN attachment or HA VPN gateway has the required stack type of `IPV4_IPV6`. If the stack type is incorrect for a VLAN attachment, modify the VLAN attachment. For a HA VPN gateway, recreate the HA VPN gateway and its tunnels.

  3. Ensure that the Cloud Router is configured correctly and that your on-premises router is configured with the matching IPv6 BGP addresses.

Run the following command:
         
         gcloud compute routers describe ROUTER-NAME
         

In the command output, check the following values:

     * `bgpPeers.peerIpAddress` is an IPv6 address assigned to the external interface on your on-premises router. This IPv6 address is used as the BGP peering address with Cloud Router for a HA VPN tunnel or a Dedicated Interconnect VLAN attachment.

     * `bgpPeers.ipAddress` is an IPv6 address assigned to the interface of the Cloud Router and matches the value configured as the peer BGP IP address on your on-premises router.

     * `bgpPeers.peerAsn` matches the ASN of your on-premises router.

     * `bgp.asn` matches the peer ASN configured on your on-premises router.




## BGP resets that originate from Google Cloud appear on your router

Cloud Router tasks are software processes in the Google Cloud control plane that are normally migrated from machine to machine. During such migrations, the Cloud Router might be down for periods of up to 60 seconds. Normal migrations don't cause traffic to be dropped.

The Cloud Router is not located in the data path and is not acting as a Layer 3 switch, but as a manager for route programming. Routing is actually handled by the VLAN attachment or the Cloud VPN tunnel.

Cloud Logging adds entries for the affected router when BGP resets occur. You can find the events by searching the Logging logs for the routing ID and using the key `textPayload="Router Event: Router task activated`.

For more information about viewing Logging logs, see [View logs and metrics](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-logs-metrics).

## On-premises router experiences BGP flap

BGP flaps can be caused by various issues, including Cloud Router [software maintenance](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/how-cloud-router-works#maintenance).

To get details about completed maintenance events, see [Identifying router maintenance events](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/identifying-router-events). To get details about other Cloud Router events, see [Viewing Cloud Router logs and metrics](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-logs-metrics).

A Cloud Router maintenance event is not indicative of a problem if your on-premises router is configured as follows:

  * The on-premises router can process graceful restart notifications.
  * The on-premises router's hold timer is set to at least 60 seconds.



For a comprehensive overview of timer settings, see [Managing BGP timers](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-bgp-timers).

For help monitoring connectivity, see [Verify connectivity between the on-premises router and the Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/identifying-router-events#verify-connectivity).

## BGP session closes

If your on-premises router advertises more than 5,000 prefixes, then the Cloud Router closes the BGP session and does not attempt to re-establish it until the BGP peering is reset manually. The following log is generated in Cloud Logging when this happens.
    
    
    BGP: Sent NOTIFICATION 6/1 (CEASE/MAX_PREFIXES_REACHED) to the peer
    "PEER_IP_ADDRESS"
    
    The BGP session from peer "PEER_IP_ADDRESS" was shut down because the number of
    received prefixes reached the limit of 5000. Please reduce the prefixes sent to
    the Cloud Router, then disable and re-enable the BGP peer.
    

To resolve this issue, do the following:

  1. Reduce the prefixes sent from your on-premises router using commands from your router's vendor.

  2. [Disable the BGP peer](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/disabling-removing-bgp#disable_a_bgp_session).

  3. [Enable the BGP peer](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/disabling-removing-bgp#enable_a_bgp_session).




## What's next

  * For more information about how to use Cloud Logging to monitor Cloud Router, see [View logs and metrics](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-logs-metrics).

  * For additional support, see [Getting support](https://docs.cloud.google.com/network-connectivity/docs/router/support/getting-support).

  * For information about BGP session states, see [BGP session states](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-states).

  * For information about diagnostic messages and session states related to Bidirectional Forwarding Detection (BFD), see [BFD diagnostic messages and session states](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd-states).

  * For issues related to using Cloud Router with Router appliance, see [Troubleshooting Router appliance](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting#troubleshooting-ra) in the Network Connectivity Center documentation.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
