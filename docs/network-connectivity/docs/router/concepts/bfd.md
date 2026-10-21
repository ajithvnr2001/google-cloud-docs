---
url: https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd/
title: Bidirectional Forwarding Detection (BFD) overview \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:23:20.067222+00:00
---

# Bidirectional Forwarding Detection (BFD) overview  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Bidirectional Forwarding Detection (BFD) overview

This page describes [Bidirectional Forwarding Detection (BFD)](https://wikipedia.org/wiki/Bidirectional_Forwarding_Detection) for Cloud Router.

BFD ([RFC 5880](https://tools.ietf.org/html/rfc5880), [RFC 5881](https://tools.ietf.org/html/rfc5881)) is a forwarding path outage detection protocol that is supported by most commercial routers. With BFD for Cloud Router, you can enable BFD functionality inside a BGP session to detect forwarding path outages such as link down events. This capability makes hybrid networks more resilient.

When you peer with Google Cloud from your on-premises network by using Dedicated Interconnect or Partner Interconnect, you can enable BFD for fast detection of link failure and failover of traffic to an alternate link that has a backup BGP session. In this way, BFD provides a high-availability network connectivity path that can respond quickly to link faults.

## BFD benefits

BFD configured with default settings detects failure in 5 seconds, compared to 60 seconds for BGP-based failure detection. With BFD implemented on Cloud Router, end-to-end detection time can be as short as 5 seconds.

BFD is a fixed-length hello protocol in which each end of a connection transmits packets periodically over a forwarding path.

BFD is a UDP-based detection protocol that provides a low-overhead method of detecting failures in the forwarding path between two adjacent routers. This includes detecting failures in interfaces, data links, and forwarding planes. You can enable BFD at the routing protocol level.

## BFD limitations

You can only enable BFD in BGP sessions that you configure for VLAN attachments in Dedicated Interconnect or Partner Interconnect. BFD is not supported in BGP sessions that are configured for HA VPN tunnels or for Router appliance, which is part of Network Connectivity Center.

**Important:** BFD can only be enabled on provisioned VLAN attachments that use Dataplane version 2. You can view the `dataplaneVersion` for a VLAN attachment by viewing the attachment details in one of the following ways:

  * **API** : Use the [interconnectAttachments.get](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnectAttachments/get) method. You can use this method on VLAN attachments for either Dedicated Interconnect or Partner Interconnect. 
  * **Google Cloud CLI** : Use the `gcloud compute interconnects attachments describe ATTACHMENT-NAME` command where ATTACHMENT-NAME is the name of the VLAN attachment for either Dedicated Interconnect or Partner Interconnect. 



In the output of the API or gcloud CLI command, look for the `dataplaneVersion` field with a value of `2`. If the field is absent from the output, the VLAN attachment is using version 1 and cannot be used with BFD. For more information, contact your customer account team.

The Cloud Interconnect Dataplane v2 is unrelated to [ Google Kubernetes Engine (GKE) Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2)

## BFD session establishment

To establish a BFD session, configure BFD on both BGP peers: a Cloud Router and your on-premises router running BFD. After you enable BFD for the BGP routing protocol on the router, a BFD session is created, BFD timers are negotiated, and the BFD peers begin to send BFD control packets to each other at the negotiated interval.

By sending rapid failure detection notices to BGP on the local router to initiate the routing table recalculation process, BFD contributes to greatly reduced overall network convergence time.

The following diagram shows a simple network with two routers running BGP and BFD. These numbers represent the BFD session establishment process:

  1. BGP neighbor is set up.
  2. BGP sends a request to the local BFD process to initiate a BFD neighbor session with the BGP peer/neighbor router.
  3. The BFD neighbor session with the BGP neighbor router is established.

[ ![BFD session establishment.](https://docs.cloud.google.com/static/network-connectivity/docs/router/images/bfd-establishment.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/router/images/bfd-establishment.svg) BFD session establishment (click to enlarge)

## BFD during a failure event

The following figure shows what happens when a failure occurs in the network.

In BFD control-only mode, the Cloud Router and your on-premises router periodically send BFD control packets to each other. If the number of control packets in a row configured in the `bfd multiplier` setting on the Cloud Router is not received by the other router, the session is declared down. Then, the following happens:

  1. A failure in the link occurs between Google Cloud and the on-premises router.
  2. The BFD neighbor session with the BGP neighbor router is torn down.
  3. BFD notifies the local BGP process that the BFD neighbor is no longer reachable.
  4. The local BGP process tears down the BGP neighbor relationship.



If an alternative path is available, the routers immediately start converging on it.

[ ![BFD during a failure event.](https://docs.cloud.google.com/static/network-connectivity/docs/router/images/bfd-during-failure.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/router/images/bfd-during-failure.svg) BFD during a failure event (click to enlarge)

## BFD dampening

Cloud Router implements BFD dampening internally to suppress the negative effect of frequent BFD session flaps on BGP. BFD dampening uses default parameters which cannot be modified by the user.

BFD dampening uses a penalty system. The penalty value starts at 0 and increases to 1 for the first flap. After the first flap, the penalty doubles each time another BFD flap occurs. When the penalty exceeds the threshold value of 4, BFD suppresses notifications to BGP. The penalty is reduced by half every 10 minutes if no flap occurs during this period.

BFD enables notifications to BGP again after the penalty goes below the re-use threshold of 4.

The maximum suppression interval for BFD notifications to BGP is 1 hour. This ensures that BFD session down notifications are not dampened forever.

## BFD asynchronous mode

Cloud Router supports an asynchronous mode of operation, where the systems involved periodically send BFD control packets to one another. If a configured number of those packets in a row are not received by the other system, the session is declared to be down.

The demand mode of BFD operation is not supported. For packet mode, BFD supports control-only mode; echo mode is not supported.

In the asynchronous mode of operation with control-only packet mode, BFD runs on the control plane and can add slight overhead and CPU processing time.

By default, BFD is disabled on Cloud Router BGP sessions. To use BFD, you must [enable it](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bfd).

In the following failure scenario, the routers have the following settings:

  * The Cloud Router's BFD minimum _receive_ and _transmit_ intervals are set to 1000 milliseconds (ms).
  * The peer router's BFD minimum _receive_ and _transmit_ intervals are set to 1000 ms.
  * The BFD RFC 5880 protocol negotiates the agreed transmit interval to the higher of the transmit interval from the sender's side and receive interval of the receiver's side. Hence, the agreed transmit intervals on either side is 1000 ms due to identical settings.
  * The detection time calculation on Cloud Router is the peer router's agreed transmit interval multiplied by the peer router's BFD multiplier value. In this scenario, the detection time is 1000 ms * 5 = 5000 ms.
  * The detection time calculation on the peer router is the Cloud Router's agreed transmit interval multiplied by the Cloud Router's BFD multiplier value. In this scenario, the detection time is 1000 ms * 5 = 5000 ms.



The Cloud Router negotiates with the peer router and expects to receive control packets every 1000 ms from the peer router. If 5000 ms pass without the Cloud Router receiving a control packet, its detect timer expires and it declares the BFD session to be down.

[ ![BFD without echo packets.](https://docs.cloud.google.com/static/network-connectivity/docs/router/images/bfd-without-echo-mode.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/router/images/bfd-without-echo-mode.svg) BFD without echo packets (click to enlarge)

We recommend the following when configuring BFD:

  * To avoid a BFD multiplier mismatch, that you configure your on-premises and Cloud Router to the same BFD settings.
  * To avoid BFD and BGP flaps, that you set the minimum BFD expired timeout no less than 5000 ms in each direction.



### Graceful restart and BFD

To minimize the impact to traffic during Cloud Router software maintenance events, we recommend that you enable BGP graceful restart.

If both BGP graceful restart and BFD are enabled, then when Cloud Router restarts it attempts to turn off BFD by sending an `AdminDown` message to the on-premises router. When this happens, the BGP session stays up on the on-premises side and the on-premises router enters graceful restart mode. While the on-premise router is in graceful restart mode, Cloud Router can restart without impacting data plane traffic.

Similarly, if the on-premises router sends an `AdminDown` message before its control plane restarts, Cloud Router enters graceful restart mode. While Cloud Router is in graceful restart mode, the on-premises router can restart without impacting data plane traffic.

Cloud Router sets the [control plane independent bit](https://www.rfc-editor.org/rfc/rfc5880.html#section-4.1) to 0 when establishing BFD with its peer router, to signal that its implementation of BFD is control-plane dependent. If an interface failure occurs, it's possible that the peer router can't distinguish between a BFD failure that's caused by a control plane failure or a data plane failure. For example, an interface failure can cause the on-premises router to enter a graceful restart mode and unnecessarily delay a traffic fail-over from the affected link.

Because of the possible BFD failure ambiguity, different vendors treat this specific scenario differently and offer configuration settings to change the default behavior. We recommend that you review your router vendor's documentation and configure your on-premises router to ensure that a BFD interface failure event with a control-plane dependent BFD peer triggers an immediate failover when used with BGP graceful restart.

## BFD settings and timers

This section describes BFD settings that you can configure on Cloud Router.

### BFD session initialization mode

Description | The BFD session initialization mode for this BGP peer.  
---|---  
`gcloud` command | `--bfd-session-initialization-mode`  
API field | `bgpPeers[].bfd.sessionInitializationMode`  
Default setting | `Disabled`  
  
There are three BFD mode settings, `Active`, `Passive`, and `Disabled`. If you don't set this mode, it defaults to a setting of `Disabled`, using non-echo mode (control packets only).

  * `Disabled` (default): BFD is disabled for this BGP peer.
  * `Passive`: The Cloud Router waits for the peer router to initiate the BFD session for this BGP peer.
  * `Active`: The Cloud Router initiates the BFD session for this BGP peer.



You must set the router on at least one side of a connection—either the Cloud Router or the peer router—to `Active`. When configuring a BGP session between two Cloud Routers, set one router's BFD session initialization mode to `Active`.

If you set both sides to `Active`, the two sides send an initial control packet to negotiate parameters, and the session is eventually established.

If you set BFD session initialization mode to `Disabled`, you can optionally configure the rest of the BFD settings. These settings take effect when you re-enable BFD.

### BFD minimum transmit interval (BFD packets to a peer)

Description | The minimum interval, in milliseconds, between BFD control packets transmitted to a BGP peer.  
---|---  
`gcloud` command | `--bfd-min-transmit-interval`  
API field | `bgpPeers[].bfd.minTransmitInterval`  
Default setting | 1000 ms. You can specify a setting between 1000 ms and 30000 ms. The BFD RFC 5880 protocol sets the agreed transmit interval as the higher value between the Cloud Router's transmit interval and the peer's receive interval. Hence, BFD is supported on BGP sessions even if your on-premises device only support a minimum receive interval that's lower than 1000 ms.  
  
### BFD minimum receive interval (BFD packets from a peer)

Description | The minimum interval, in milliseconds, between BFD control packets received from a BGP peer.  
---|---  
`gcloud` command | `--bfd-min-receive-interval`  
API field | `bgpPeers[].bfd.minReceiveInterval`  
Default setting | 1000 ms. You can specify a setting between 1000 ms and 30000 ms. The BFD RFC 5880 protocol sets the agreed transmit interval from the peer router as the higher value between the peer's transmit interval and the Cloud Router's receive interval. Hence, BFD is supported on BGP sessions even if your on-premises device only support a minimum transmit interval that's lower than 1000 ms.  
  
### BFD multiplier

Description | The number of consecutive BFD control packets that must be missed before BFD declares that a peer is unavailable. This multiplier is used to calculate the detection time on the receiving side as follows: Detection time = Agreed transmit interval * BFD multiplier  
---|---  
`gcloud` command | `--bfd-multiplier`  
API field | `bgpPeers[].bfd.multiplier`  
Default setting | 5 packets. You can specify a setting between 5 packets and 16 packets. To achieve identical detection times in both directions, set the same multiplier value on both the Cloud Router and your peer router.  
  
## What's next

  * To update BFD settings, see [Update or disable BFD](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/updating-bfd).

  * To configure BFD, see [Configure BFD](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bfd).

  * To find examples of third-party router configurations that support BFD for Cloud Router, see [Use third-party router configurations for BFD](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bfd-interop).

  * For help with BFD diagnostic messages, session states, and status messages, see [BFD diagnostic messages and session states](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd-states).

  * To troubleshoot issues with Cloud Router, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/router/resources/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
