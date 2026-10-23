---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bfd/
title: Configure BFD for Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:50.819747+00:00
---

# Configure BFD for Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bfd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure BFD for Cloud Router

With Bidirectional Forwarding Detection (BFD) for Cloud Router, you can quickly detect forwarding path outages such as BGP up or down events, allowing for more resilient hybrid networks.

You can configure BFD in BGP sessions for VLAN attachments. BFD is not supported in BGP sessions that are configured for HA VPN tunnels or for Router appliance, which is part of Network Connectivity Center.

To learn more about BFD, see the [Bidirectional Forwarding Detection (BFD) for Cloud Router overview](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd), which includes full descriptions of [BFD settings and timers](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd#bfd-settings).

**Note:** Cloud Router supports only BFD single-hop mode. BFD multi-hop and BFD auth are not supported. If the on-premises router inherits the BFD mode from the eBGP multi-hop configuration, then configure BFD single-hop mode explicitly. Alternatively, consider removing eBGP multi-hop configuration because it is not needed on VLAN attachments that use Dataplane version 2, which is required for BFD. 

The Cisco command for setting a single-hop link is `neighbor x.y.y.z fall-over bfd single-hop`.

**Important:** BFD can only be enabled on provisioned VLAN attachments that use Dataplane version 2. You can view the `dataplaneVersion` for a VLAN attachment by viewing the attachment details in one of the following ways:

  * **API** : Use the [interconnectAttachments.get](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnectAttachments/get) method. You can use this method on VLAN attachments for either Dedicated Interconnect or Partner Interconnect. 
  * **Google Cloud CLI** : Use the `gcloud compute interconnects attachments describe ATTACHMENT-NAME` command where ATTACHMENT-NAME is the name of the VLAN attachment for either Dedicated Interconnect or Partner Interconnect. 



In the output of the API or gcloud CLI command, look for the `dataplaneVersion` field with a value of `2`. If the field is absent from the output, the VLAN attachment is using version 1 and cannot be used with BFD. For more information, contact your customer account team.

The Cloud Interconnect Dataplane v2 is unrelated to [ Google Kubernetes Engine (GKE) Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2)

## Before you begin

###  gcloud 

If you want to use the command-line examples in this guide, do the following:

  1. Install or update to the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute).
  2. Set a [default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



###  API 

If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/compute/docs/api/prereqs).

### Add a Cloud Router to Cloud Interconnect

Before you can configure BFD, you must set up one of the following connectivity choices, which includes adding a Cloud Router with a BGP session:

  * [A Dedicated Interconnect connection](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview)
  * [A Partner Interconnect connection](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/provisioning-overview)



## Configure BFD on an existing BGP session

You can configure BFD on a BGP session that was previously set up for a VLAN attachment.

**Note:** The peer router is your non-Google Cloud router that establishes a BGP session with a Cloud Router.

To configure BFD settings on an existing BGP session, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the Cloud Router to update.

  3. On the **Router details** page, in the **BGP sessions** section, select the BGP session to update.

  4. On the **BGP session details** page, click edit**Edit**.

  5. Complete any non-BFD settings.

  6. Under **Bidirectional Forwarding Detection** , configure BFD options as documented in [BFD settings and timers](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd#bfd-settings).

**Required:** To enable BFD, set **BFD session initialization mode** to `active`.




###  gcloud 

Run the `update-bgp-peer` command:
    
    
    gcloud compute routers update-bgp-peer ROUTER_NAME \
        --project=PROJECT_ID \
        --peer-name=PEER_NAME \
        --interface=INTERFACE \
        --ip-address=IP_ADDRESS \
        --peer-asn=PEER_ASN \
        --peer-ip-address=PEER_IP_ADDRESS \
        --region=REGION \
        --bfd-session-initialization-mode=BFD_SESSION_INITIALIZATION_MODE  \
        --bfd-min-receive-interval=BFD_MIN_RECEIVE_INTERVAL \
        --bfd-min-transmit-interval=BFD_MIN_TRANSMIT_INTERVAL \
        --bfd-multiplier=BFD_MULTIPLIER
    

Replace the following:

  * `ROUTER_NAME`: the name of your Cloud Router
  * `PROJECT_ID`: the project that contains your Cloud Router
  * `PEER_NAME`: the name of your BGP peer
  * `INTERFACE`: the name of the interface for this BGP peer
  * `IP_ADDRESS`: the IP address for your Cloud Router
  * `PEER_ASN`: the BGP autonomous system number (ASN) for this BGP peer
  * `PEER_IP_ADDRESS`: the link-local address of the peer router belonging to the range `169.254.0.0/16`
  * `REGION`: the region where the Cloud Router is located
  * Configure BFD options as documented in [BFD settings and timers](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd#bfd-settings).

**Required:** To enable BFD, set `BFD_SESSION_INITIALIZATION_MODE` to `active`.




###  API 

Use the [`routers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) method to update the `bgpPeers[].bfd` field.

The `bgpPeers[]` field accepts an array of BGP peers. When you `PATCH` this field, you overwrite the existing array of BGP peers with the new array included in your request.

  1. Send a `GET` request to get the current array of BGP peers for the router. For details, see [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration).

  2. Send a `PATCH` request with a new array of BGP peers. In the array element that contains the BGP session whose BFD settings you want to update, modify the `bgpPeers[].bfd` field:
         
         PATCH https://compute.googleapis.com/compute/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
            {
              "bgpPeers": [
                BGP_PEERS
              ]
            }
         

Replace the following:

     * `PROJECT_ID`: the project that contains the Cloud Router
     * `REGION`: the region where the Cloud Router is located
     * `ROUTER_NAME`: the name of the Cloud Router
     * `BGP_PEERS`: the contents of the new array of BGP peers

The following example includes two BGP peers and sets the values in the `bgpPeers[].bfd` field. For more information about these options, see [BFD settings and timers](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd#bfd-settings).

**Required:** To enable BFD, set `sessionInitializationMode` to `ACTIVE`.
    
    {
          "name": "peer-1",
          "interfaceName": "if-peer-1",
          "ipAddress": "169.254.10.1",
          "peerIpAddress": "169.254.10.2",
          "peerAsn": 64512,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT"
          **"bfd": {
            "sessionInitializationMode": ACTIVE,
            "minTransmitInterval": 1000,
            "minReceiveInterval": 1000,
            "multiplier": 5
          }**
        },
        {
          "name": "peer-2",
          "interfaceName": "if-peer-2",
          "ipAddress": "169.254.20.1",
          "peerIpAddress": "169.254.20.2",
          "peerAsn": 64513,
          "advertisedRoutePriority": 99,
          "advertiseMode": "DEFAULT"
          **"bfd": {
            "sessionInitializationMode": ACTIVE,
            "minTransmitInterval": 1000,
            "minReceiveInterval": 1000,
            "multiplier": 5
          }**
        }
    




## Configure BFD on your peer router

To enable BFD on your peer router, use your vendor's recommended configuration and commands to set the following:

  * Minimum transmit interval
  * Minimum receive interval
  * Detection multiplier



We recommend that you keep the values of the BFD parameters identical to the corresponding Cloud Router values.

When configuring BFD detection intervals, consider the following:

  * For BFD timer negotiation between BFD peers, the slower of the two peers determines the transmission rate.

  * Cloud Router supports 1000ms for the minimum `transmit` and `receive` intervals.

    * You can configure higher values on your router, which forces the effective transmit and receive intervals to be longer, not shorter.
  * The overall BFD detection interval on the receiving side is the product of the detection multiplier of the sender and the effective transmit interval of the sender.

    * Cloud Router's minimum value for the multiplier is five.
  * The effective transmit interval on your router is equal to or greater than 1000ms due to slower negotiated values between Cloud Router and the peer. Cloud Router's minimum transmit interval is 1000ms.

    * If the `transmit interval` setting is less than `1000ms` in your router, then set the multiplier to at least five.
    * If the `transmit interval` setting is greater than `1000ms` then set the multiplier high enough that the `transmit` interval * `multiplier` is at least five seconds.



Following is a sample BFD configuration for a Cisco router. For additional configuration examples, see [Use third-party router configurations for BFD](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bfd-interop).
    
    
      int range <physical interface>
        bfd interval 1000 min_rx 1000 multiplier 5
    
      router bgp <ASN>
        neighbor 169.254.33.6 fall-over bfd
        neighbor 169.254.44.6 fall-over bfd
    

## Verify BFD on your peer router

After configuring your peer router, verify if the session to the Cloud Router is up and running by viewing details about the BFD session.

  * The following sample command for a Cisco router shows the status of the BFD session:
        
        show bfd neighbors 169.254.44.6 details
        

  * The command output should look like the following example:
        
        IPv4 Sessions
        NeighAddr                    LD/RD           RH/RS     State     Int
        169.254.44.6                 4212/2045617738 Up        Up        Tu503
        Session state is UP and not using echo function.
        Session Host: Software
        OurAddr: 169.254.44.5
        Handle: 4
        Local Diag: 0, Demand mode: 0, Poll bit: 0
        MinTxInt: 1000, MinRxInt: 1000, Multiplier: 5
        Received MinRxInt: 1000, Received Multiplier: 5
        Holddown (hits): 244(1), Hello (hits): 100(30409)
        Rx Count: 4562, Rx Interval (ms) min/max/avg: 10/1140/870 last: 56 ms ago
        Tx Count: 4475, Tx Interval (ms) min/max/avg: 10/1040/890 last: 64 ms ago
        Elapsed time watermarks: 4 4 (last: 4)
        Registered protocols: CEF BGP
        Uptime: 00:06:39
        Last packet: Version: 1                  - Diagnostic: 0
                     State bit: Up               - Demand bit: 0
                     Poll bit: 0                 - Final bit: 0
                     C bit: 0
                     Multiplier: 5               - Length: 24
                     My Discr.: 2045617738       - Your Discr.: 4212
                     Min tx interval: 1000     - Min rx interval: 1000
                     Min Echo interval: 0
        

  * This sample output from a Cisco ASR peer router shows the diagnostic information that you can view on the peer side to determine the status of your BFD session:
        
        14:06:12.906921 IP (tos 0xc0, ttl 255, id 58754, offset 0, flags [none], proto UDP (17), length 52)
          169.254.44.5.49152 > 169.254.44.6.3784: [udp sum ok] BFDv1, length: 24
        Control, State Down, Flags: [none], Diagnostic: No Diagnostic (0x00)
        Detection Timer Multiplier: 5 (5000 ms Detection time), BFD Length: 24
        My Discriminator: 0x0000100b, Your Discriminator: 0x00000000
          Desired min Tx Interval:    1000 ms
          Required min Rx Interval:   1000 ms
          Required min Echo Interval:  100 ms
        




## Verify BFD on the Cloud Router

Verify the BFD session on the Google Cloud side by using one of the following methods:

  * For a session state change, [check the logs generated in Cloud Logging](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-logs-metrics#logs), or check the [Cloud Monitoring metric for `bfd/session_up`](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-logs-metrics#monitoring-metrics).

  * For information about the BFD session, view the [Cloud Router status](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#viewing-router-status).




## What's next

  * To modify BFD settings on a BGP session, see [Update or disable BFD](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/updating-bfd).

  * For help with BFD diagnostic messages, session states, and status messages, see [BFD diagnostic messages and session states](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd-states).

  * To troubleshoot issues with Cloud Router, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/router/resources/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
