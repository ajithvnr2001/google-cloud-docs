---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting/
title: Troubleshooting \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:06.232242+00:00
---

# Troubleshooting  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

This troubleshooting guide can help you solve common issues that you might encounter when using Cloud Interconnect:

  * General troubleshooting
  * Dedicated Interconnect
  * Partner Interconnect
  * HA VPN over Cloud Interconnect
  * [MACsec for Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/macsec/troubleshoot-macsec)
  * Cross-Cloud Interconnect



For answers to common questions about Cloud Interconnect architecture and features, see the [Cloud Interconnect FAQ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/faq).

For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

**Important:** BFD can only be enabled on provisioned VLAN attachments that use Dataplane version 2. You can view the `dataplaneVersion` for a VLAN attachment by viewing the attachment details in one of the following ways:

  * **API** : Use the [interconnectAttachments.get](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnectAttachments/get) method. You can use this method on VLAN attachments for either Dedicated Interconnect or Partner Interconnect. 
  * **Google Cloud CLI** : Use the `gcloud compute interconnects attachments describe ATTACHMENT-NAME` command where ATTACHMENT-NAME is the name of the VLAN attachment for either Dedicated Interconnect or Partner Interconnect. 



In the output of the API or gcloud CLI command, look for the `dataplaneVersion` field with a value of `2`. If the field is absent from the output, the VLAN attachment is using version 1 and cannot be used with BFD. For more information, contact your customer account team.

The Cloud Interconnect Dataplane v2 is unrelated to [ Google Kubernetes Engine (GKE) Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2)

To find logging and monitoring information and view Cloud Interconnect metrics, see [Monitoring connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/monitoring).

## General troubleshooting

### Check for Cloud Interconnect service disruptions

  * You can check known disruptions on the [Google Cloud Status Dashboard](https://status.cloud.google.com/). You can also subscribe to the Cloud Incidents [JSON feed](https://status.cloud.google.com/incidents.json) or [RSS feed](https://status.cloud.google.com/en/feed.atom) for push updates.

  * You are notified of maintenance events on that impact your Dedicated Interconnect connections. For details, see [Infrastructure maintenance events](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/infrastructure-maintenance-events).

  * You are notified of maintenance events that impact your Partner Interconnect VLAN attachments. Notifications for Partner Interconnect are sent in a similar fashion as the notifications for Dedicated Interconnect connections with some minor differences. For details, see [Infrastructure maintenance events](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/faq#maintenance-event-notice).




### Can't connect to resources in other regions

By default, Virtual Private Cloud (VPC) networks are regional, meaning that Cloud Router advertises only the subnets in its region. To connect to other regions, set the dynamic routing mode of your VPC network to global so that Cloud Router can advertise all subnets.

For more information, see [Dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#dynamic-routing-mode-effects-on-learned-routes) in the Cloud Router documentation.

### Can't reach VMs in a peered VPC network

In this scenario, you have set up a Cloud Interconnect connection between your on-premises network and a VPC network, _network A_. You have also set up VPC Network Peering between _network A_ and another VPC network, _network B_. However, you are unable to reach VMs in _network B_ from your on-premises network.

This configuration is unsupported as described in the [restrictions](https://docs.cloud.google.com/vpc/docs/vpc-peering#restrictions) of the VPC Network Peering overview.

However, you can use custom IP range advertisements from Cloud Routers in your VPC network to share routes to destinations in the peer network. In addition, you must configure your VPC Network Peering connections to import and export custom routes.

For more information about advertising routes between on-premises networks and VPC peered networks, see the following resources:

  * [Advertising custom IP ranges](https://docs.cloud.google.com/router/how-to/advertising-custom-ip#gcloud)
  * [Troubleshooting](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#troubleshooting) in Using VPC Network Peering



### Missing subnets in a connection

To advertise all of the available subnets, specify the missing routes with custom advertised routes and advertise all subnet routes between regions with global dynamic routing. To do this, follow these steps:

  1. Specify custom advertised routes on both a Cloud Router and the Border Gateway Protocol (BGP) session.

To enter the missing routes, set the following parameters:
         
         --set-advertisement-groups = ADVERTISED_GROUPS
         --set-advertisement-ranges = ADVERTISED_IP_RANGES
         

Replace the following:

     * `ADVERTISED_GROUPS`: a Google-defined group that Cloud Router dynamically advertises; it can have a value of `all_subnets`, which mimics the default behavior of a Cloud Router
     * `ADVERTISED_IP_RANGES`: the contents of the new array of IP address ranges; it can have one or more values of your choice

For more details and examples, see [Advertising custom IP ranges](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip).

  2. Enable [global dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-network-set-modes).




### Can't ping Cloud Router

If you can't ping Cloud Router from your on-premises router, find your product in the following table and perform the troubleshooting steps for that product. VMs cannot reach `169.254.0.0/16`.

Troubleshooting steps to follow | Dedicated Interconnect | Partner Interconnect with L3 partner | Partner Interconnect with L2 partner  
---|---|---|---  
For Partner Interconnect, the Cloud Router might never be pingable because some partners filter traffic to the IP range (`169.254.0.0/16`) for Cloud Router. For L3 partners, the partner automatically configures BGP. If BGP doesn't come up, contact your partner. | Not applicable | Yes | Not applicable  
Verify that your local device has learned the correct MAC address for the Google Cloud side of the connection. For more information, see Troubleshooting ARP. | Yes | Not applicable | Not applicable  
Verify that your Cloud Router has an interface and a BGP peer. Cloud Router is not pingable unless the interface and BGP peer are fully configured, _including the remote ASN_. 

  * For Dedicated Interconnect, see BGP session not working.
  * For L2 Partner Interconnect, Google has added the interface and BGP peer for Cloud Router automatically, but you must configure the remote ASN.

| Yes | Not applicable | Yes  
  
#### Troubleshooting ARP

For Dedicated Interconnect, to find the correct MAC address, run the following `gcloud` command:
    
    
      gcloud compute interconnects get-diagnostics INTERCONNECT_NAME
    

The `googleSystemID` contains the MAC address that should be present in your device's ARP table for IP addresses assigned to Cloud Router.
    
    
      result:
        links:
        — circuitId: SAMPLE-0
          googleDemarc: sample-local-demarc-0
          lacpStatus:
            googleSystemId: ''
            neighborSystemId: ''
            state: DETACHED
          receivingOpticalPower:
            value: 0.0
          transmittingOpticalPower:
            value: 0.0
        macAddress: 00:00:00:00:00:00
    

If your device has not learned a MAC address, verify that the correct VLAN ID and IP address are configured on the subinterface.

For Partner Interconnect, if you see the wrong MAC address on your device, verify that you have not bridged the Layer 2 segments of two VLAN attachments. The Google Cloud side of the Cloud Interconnect connection is configured with [ip proxy-arp](https://wikipedia.org/wiki/Proxy_ARP), which replies to all ARP requests and can cause your on-premises router to learn incorrect ARP entries.

### Can't create VLAN attachment

If you attempt to [create a VLAN attachment for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments) or [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments) that violates an organization policy, you see an error message. See the following example error message from running `gcloud compute interconnects attachments partner create`:
    
    
    ERROR: (gcloud.compute.interconnects.attachments.partner.create) Could not fetch resource:
    - Constraint constraints/compute.restrictPartnerInterconnectUsage violated for projects/example-project. projects/example-project/global/networks/example-network is not allowed to use the Partner Interconnect.
    

For more information, see [Restrict Cloud Interconnect usage](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/restricting-usage) and [Use custom organization policies](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/custom-constraints) and contact your organization administrator.

### Share connections with other projects in my organization

Use Shared VPC to share a connection, such as a VLAN attachment or a Dedicated Interconnect connection in a host project.

For more information about setting up a Shared VPC network, see [Provisioning Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc).

For more information about configuring attachments in a Shared VPC network, see [Options for connecting to multiple VPC networks](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/enabling-multiple-networks-access-same-attachment).

## Dedicated Interconnect

### Google can't ping you during the connection provisioning process

Check that you're using the correct IP and LACP configuration. During the testing process, Google sends you different test IP configurations for your on-premises router, depending on whether you order a multiple-link bundle or a single-link bundle. Don't configure VLAN attachments for either of these tests.

#### For multiple-link bundles

  * The first set of IP addresses that Google sends is for [testing multi-circuit connectivity](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/testing-connections#test-multi-circuit) on each individual link. Configure the test IP addresses on every physical link (without LACP configured), as instructed in the emails that Google sent you. Google must ping all the IP addresses successfully before this first test passes.
  * For the second test, remove all the IP addresses from the first test. _Configure the port channel with LACP even if your connection has only one link._ Google pings the port channel address. Don't modify the LACP configuration of your port channel after the connection has passed the final test. However, you must remove the test IP address from the port channel interface.



#### For single-link bundles

  * Google sends the final production IP address for [testing single-circuit connectivity](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/testing-connections#test-single-circuit). Configure the IP address on the bundle interface (with LACP configured, either active or passive mode), as instructed in the email that Google sent you. Google must ping the bundle interface IP address successfully before this test passes. _Configure the port channel with LACP even if your connection has only one link._



### Can't ping Cloud Router

  * Check that you can ping Google's port channel IP address. The IP address is the `googleIpAddress` value when you [view connection details](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/viewing-interconnects).
  * Check that you have the correct VLAN on your on-premises router's subinterface. The VLAN information should match the information provided by the [VLAN attachment](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments).
  * Check that you have the right IP address on your on-premises router's subinterface. When you create a VLAN attachment, it allocates a pair of link-local IP addresses. One is for an interface on a Cloud Router (`cloudRouterIpAddress`), and the other is for a subinterface on your on-premises router's port channel, not the port channel itself (`customerRouterIpAddress`).
  * If you're testing the performance of your VLAN attachments, don't ping Cloud Router. Instead, create and then use a Compute Engine virtual machine (VM) instance in your VPC network. For more information, see Performance testing.



### BGP session not working

  * Enable multi-hop BGP on your on-premises router with at least two hops.
  * Check that you have the correct neighbor IP address configured on your on-premises router. Use the BGP peer IP address (`cloudRouterIpAddress`) that the VLAN attachment allocated.
  * Check that the local ASN configuration on your on-premises router matches the peer ASN on the Cloud Router. In addition, check that the local ASN configuration on the Cloud Router matches the peer ASN on your on-premises router.
  * Each attachment is allocated a unique /29 CIDR from `169.254.0.0/16` within your VPC network. One IP address in the /29 CIDR is allocated for the Cloud Router and the other for your on-premises router.

Check that the correct IP addresses are allocated for your on-premises router interface and its BGP neighbor. A common mistake is to configure a /30 on your on-premises router interface instead of a /29. Google Cloud reserves all other addresses in the /29 CIDR.

Make sure that you have not allocated any other IP addresses from this CIDR to the VLAN attachment interface on your router.




### Can't reach VMs in your VPC network

  * Check that you can ping the port channel and VLAN attachment.
  * Check that your BGP session is active.
  * Check that your on-premises router is advertising and receiving routes.
  * Check that there are no overlaps between your on-premises route advertisements and Google Cloud network ranges.
  * Set the MTU size to the same values for your on-premises router, VPC, and VLAN attachment.



### IPv6 traffic is not passing over the VLAN attachment

If you are experiencing difficulty connecting to IPv6 hosts, do the following:

  1. Verify that IPv6 routes are being correctly advertised. If IPv6 routes are not being advertised, see [Troubleshoot BGP routes and route selection](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-routes).
  2. Inspect [firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls) to ensure that you are allowing IPv6 traffic.
  3. Verify that you do not have overlapping IPv6 subnet ranges in your VPC network and your on-premises network. See [Check overlapping subnet ranges](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-routes#overlap-ranges).
  4. Determine whether you have exceeded any quotas and limits for your learned routes in Cloud Router. If you have exceeded your quota for learned routes, IPv6 prefixes are dropped before IPv4 prefixes. See [Check quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-routes#check-quotas-and-limits).
  5. Verify that all components related to IPv6 configuration have been configured correctly.

     * The VPC network has enabled the use of internal IPv6 addresses with the `--enable-ula-internal-ipv6` flag.
     * The VPC subnet is configured to use the `IPV4_IPV6` stack type.
     * The VPC subnet has`--ipv6-access-type` set to `INTERNAL`.
     * The Compute Engine VMs on the subnet are configured with IPv6 addresses.
     * The VLAN attachment is configured to use the `IPV4_IPV6` stack type.
     * The BGP peer has enabled IPv6 and correct IPv6 next hop addresses are configured for the BGP session.

       * To view Cloud Router status and routes, see [View Cloud Router status and routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#viewing-router-status).
       * To view BGP session configuration, see [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration).



### Performance testing over your VLAN attachments

If you need to test the performance of your VLAN attachments, use a VM in your VPC network. Add the performance tools that you require on the VM. Don't use the Cloud Router link-local IP address to test for latency, such as ICMP ping or path MTU. Using Cloud Router can give unpredictable results.

### Get diagnostics

To get current, detailed technical information about the Google Cloud side of a Dedicated Interconnect connection on demand, see [Get diagnostics](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/getting-diagnostics).

### Issues with Letter of Authorization (LOA)

These subsections cover issues concerning the LOA.

#### Haven't received the LOA within 3 business days of order confirmation

Check your email's spam or junk folder. If you still can't find the LOA, reply to the `order_received` email to contact Cloud Customer Care for assistance.

#### Colocation vendor requires clarification on the LOA details

Act as a liaison between the vendor and Google. Reply to the email notification with the vendor's specific questions, and Cloud Customer Care can help you clarify details.

#### Incorrect cross-connect installation

The connection must be made exactly as specified in the latest LOA; any deviation will result in connection failure. Often, configuration issues that are caused by deviation from the LOA return a "No Light Detected" error. See Received "No light detected" error for more information.

### Received a "No light detected" error

When you receive a "No light detected" error, it means that Google's automated testing doesn't detect sufficient optical light from your on-premises router on one or more ports. This indicates a problem at the physical layer (Layer 1). Use the following steps to troubleshoot the issue:

  1. **Verify cross-connect installation** : contact your colocation vendor, and confirm that the following is true:

     * The cross-connect installation is complete.
     * The connection adheres to the ports specified in the latest version of the LOA on the Google demarc side.
     * The vendor has test results, including light level readings taken with an optical power meter at the Google demarc, looking towards your equipment.
  2. **Inspect your physical infrastructure** : check the following components:

     * Ensure that your fiber patch cords are the correct type and are securely connected to your router's ports, as well as to any intermediate patch panels within your rack. Look for any signs of damage, sharp bends, or kinks in the cables.
     * Check your transceivers (like SFPs and QSFPs): 
       * Confirm that the transceiver model is compatible with your router and the Dedicated Interconnect speed that you ordered.
       * Ensure that the transceiver is firmly seated in the router port.
       * Try reseating the transceiver. If you have a spare transceiver, you can try swapping it.
     * Check the physical port LEDs on your router. A link light should be illuminated (usually green) if a signal is being detected. No light, or an amber light, often indicates a problem.
     * Use appropriate fiber optic cleaning tools (like cleaning pens) to clean the fiber cable ends and the transceiver optical interfaces. Dust and contaminants are very common causes of signal loss.
  3. **Check the configuration of your router ports** : ensure that the interface on your router is administratively enabled. It shouldn't be in a "shutdown" state. Use the following commands to check the status, depending on your router:

     * **Cisco IOS/NX-OS** : Use the `show interface [interface]` command. If it shows "administratively down", enter interface configuration mode and use the `no shutdown` command.
     * **Juniper Junos** : Use the `show interfaces [interface]` command. The "Admin link" should be "Up". You can enable it with the `set interfaces [interface] enable` command in configuration mode if necessary.
     * **Arista EOS** : Use the `show interface [interface] status` command. If it shows "disabled", enter interface configuration mode and use the `no shutdown` command.
  4. **Analyze light levels on your router** : access your router's CLI to check the optical transmit (`TX`) and receive (`RX`) power levels. You can use the following example commands to check power levels, depending on your router manufacturer:

     * **Cisco** : `show interface [interface] transceiver details`
     * **Juniper** : `show interfaces diagnostics optics [interface]`
     * **Arista** : `show interface [interface] transceiver dom`

After you use the command, use the following guidance to interpret the information:

     * **TX Power** : This is the power that your router is transmitting. It should be within the transceiver's specification (typically -5 to +2 dBm for standard LR optics). Very low TX power suggests a faulty optic or port on your side.
     * **RX Power** : This is the power that your router is receiving from Google's side. Use the following power ranges to assess the quality of the link: 
       * **Good** : Between -1 dBm and -10 dBm.
       * **Marginal** : Between -10 dBm and -14 dBm. The link might be unstable.
       * **No Signal** : Less than -15 dBm, often showing as -30 dBm, -40 dBm, or "Low", indicates little to no light is being received. This strongly points to a physical break, misconnection, or a polarity issue.
  5. **Test fiber polarity** : fiber optic connections require a "crossover." The `transmit` fiber from your router must connect to the `receive` fiber at the Google demarc, and the `transmit` fiber from the Google demarc must connect to the `receive` fiber at your router.

To resolve polarity issues, at your router or your patch panel try carefully "rolling" the fiber connector, swapping the positions of the two fiber strands within the duplex connector. If the link light turns on, or if RX levels improve dramatically, then you have resolved a polarity issue.

  6. **Perform loopback tests** : you can perform local and remote loopback tests to isolate which side of the connection is experiencing issues:

     * **Local loopback** : use a physical fiber optic loopback plug on your router port. This directs the router's TX signal back into its own RX port. If the port status changes to "up", your router port and transceiver are likely functioning correctly.
     * **Remote loopback (with vendor)** : request that your colocation vendor place a physical loopback on the fiber at the Google demarc, facing your equipment. If your router port comes up, this indicates that the path from your router to the Google demarc is good, and that the issue might be on Google's side of the demarc.
  7. **Check diagnostics** : you can use the following command to get diagnostic information from Google's side of the connection:
         
         gcloud compute interconnects get-diagnostics INTERCONNECT_NAME
            --project=PROJECT_ID
         

Replace the following:

     * `INTERCONNECT_NAME`: the unique name that you assigned to your Dedicated Interconnect connection.
     * `PROJECT_ID`: the ID of your project.

In the output, chcek the `receivingOpticalPower` and `transmittingOpticalPower` values for each link in the links array. These values show what Google's equipment sees. Compare Google's RX power with your router's TX power, and compare Google's TX power with your router's RX power, accounting for some signal loss over the fiber.

  8. **Gather information for Customer Care** : if you have tried the preceding steps and your issues persist, we recommend that you reply to the order email with the following information:

     * Confirmation from the colocation vendor that the cross-connect is installed as per the latest LOA.
     * Any test results provided by the vendor (like light meter readings at the demarc).
     * The full configuration of the relevant interfaces on your router.
     * The complete output of the light level diagnostic commands from your router (like the output of `show interface transceiver details`).
     * The complete JSON output of `gcloud compute interconnects get-diagnostics`.
     * The detailed results of any polarity swaps or loopback tests performed.
     * Any alarms or errors reported by your router logs for the interface(s).



### LACP configuration not working

Use the steps in this section to check for issues with your Link Aggregation Control Protocol (LACP) bundle configuration.

  1. **Verify LACP configuration on your router** : check the following LACP settings on your router:

     * All physical interfaces that are part of your Dedicated Interconnect connection must be bundled into a single Link Aggregation Group (LAG).
     * LACP must be set to **ACTIVE** mode on your router. Google uses LACP Active mode. Setting your side to **PASSIVE** mode will prevent the LACP bundle from forming.
     * Set LACP timers **FAST (1 second)** or an equivalent setting on your device. Slow timers (30 seconds) might delay bundle formation and fail automated tests.
     * Configure member ports using the following commands or command combinations, depending on your router: 
       * **Cisco** : `interface [interface]`, then `channel-group [number] mode active`
       * **Juniper** : `set interfaces [interface] gigether-options 802.3ad ae[number]`
       * **Arista** : `interface [interface]`, then `channel-group [number] mode active`
     * If you use a Juniper router, perform LAG interface configuration with the following commands: `set interfaces ae[number] aggregated-ether-options lacp active,` then `set interfaces ae[number] aggregated-ether-options lacp periodic fast`.
  2. **Analyze LACP status** : use the following commands or command combinations to check the LACP state of your router, depending on your router manufacturer:

     * **Cisco** : `show lacp neighbor`, then `show lacp internal`, then `show etherchannel summary`.
     * **Juniper** : `show lacp interfaces ae[number]`.
     * **Arista** : `show port-channel [number] lacp neighbor`, then `show etherchannel`.

     * Verify that your router shows Google's System ID as its LACP partner.

     * Verify that member ports should be in an "Collecting Distributing" state (often shown as "Bundled", "Active", or "Up"). States like "Detached", "Waiting", "Init", or "Suspended" indicate an LACP negotiation problem.

     * Verify that LACP Data Units (LACPDU) counters are incrementing, which indicates that LACP messages are being exchanged between your router and Google.

  3. **Gather information for Customer Care** : if you have tried the preceding steps and your issues persist, we recommend that you reply to the order email with the following information:

     * The full LACP configuration from your router.
     * The complete output of LACP status/neighbor commands (like `show lacp neighbor`).



### IP address connectivity not working

Use the following steps to test IP connectivity:

  1. The temporary test IP address and subnet mask that were provided to you in the `productionConfig` email must be configured directly on the logical LAG interface (like Port-Channel on Cisco/Arista, AE interface on Juniper), NOT on the physical member interfaces. Use the following commands or command combinations to verify that you have configured the test IP addresses correctly, depending on your router manufacturer:

     * **Cisco** : `show running-config interface port-channel [number]`, then `show ip interface port-channel [number]`
     * **Juniper** : `show configuration interfaces ae[number] unit 0 family inet`, then `show interfaces terse ae[number].0`
     * **Arista** : `show running-config interface port-channel [number]`, then `show ip interface port-channel [number]`
  2. Check your router's ARP table to see if it has resolved the MAC address for the Google-side test IP on the LAG interface. Use the following commands:

     * **Cisco** : `show arp | include [Google Test IP]`
     * **Juniper** : `show arp no-resolve | match [Google Test IP]`
     * **Arista** : `show arp | grep [Google Test IP]`

An "Incomplete" ARP entry indicates a Layer 2 issue, or that Google isn't responding to ARP requests.

  3. Perform a ping test from your router's LAG interface to the Google test IP. Use the ping from your LAG interface's assigned test IP address. When you've retrieved the IP address, use the following commands depending on your router's manufacturer:

     * **Cisco/Arista** : `ping [Google Test IP] source [Your LAG Test IP]`
     * **Juniper** : `ping [Google Test IP] source [Your LAG Test IP]`
  4. Ensure that no firewalls, access control lists (ACLs), or security policies on your router are blocking LACP (LACP uses EtherType 0x8809) or ICMP Echo/Reply (ping).

  5. Check the LACP status of your router by using the following command:
         
         gcloud compute interconnects get-diagnostics INTERCONNECT_NAME
            --project=PROJECT_ID
         

Replace the following:

     * `INTERCONNECT_NAME`: the unique name that you assigned to your Dedicated Interconnect connection.
     * `PROJECT_ID`: the ID of your project.

Examine the `lacpStatus` field for each of your links. The `state`, `googleSystemId`, and `neighborSystemId` values indicate whether Google sees your router as an LACP partner, and whether the states are synchronized. Then, check the `arpCache` array to see if Google's side has resolved the ARP for your test IP address.

  6. **Gather information for Customer Care** : if you have tried the preceding steps and your issues persist, we recommend that you reply to the order email with the following information:

     * The IP configuration of the LAG interface.
     * The output of the ARP table on the LAG.
     * The results of the source-based ping test from the LAG interface.
     * Confirmation that no firewalls/ACLs are blocking LACP or ICMP.
     * The complete JSON output of the `gcloud compute interconnects get-diagnostics` command.



## Partner Interconnect

### BGP session not working (Layer 2 connections)

  * Check that your on-premises router has been configured with a BGP session to your Cloud Routers. For more information, see [Configuring on-premises routers for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/configuring-onprem-routers).
  * Enable multi-hop BGP on your on-premises router with at least two hops.
  * Check that you have the correct neighbor IP address configured on your on-premises router. Use the BGP peer IP address (`cloudRouterIpAddress`) that the VLAN attachment allocated.
  * Check that the local ASN configuration on your on-premises router matches the peer ASN on the Cloud Router (`16550`). In addition, check that the local ASN configuration on the Cloud Router matches the peer ASN on your on-premises router.



### BGP session not working (Layer 3 connections)

  * Your Cloud Router must be configured with your service provider's ASN. Contact your service provider for assistance.



### VLAN attachment down for a Partner Interconnect connection

The status for a VLAN attachment can show as down even if there are no issues with the Google Cloud configuration and the Partner Interconnect connection.

Make sure that you have configured EBGP multihop on your on-premises router to have at least four hops. You can see a [sample configuration in _Configuring on-premises routers_](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/configuring-onprem-routers#device_configuration).

### Pairing key issue in a Partner Interconnect connection

When you try to set up a Partner Interconnect connection, you might encounter an error message such as "Google - Provider status not available." To fix this issue, follow these steps:

  1. Ensure that the pairing key was generated by the customer-side VLAN attachment (`PARTNER` type). The key is a long random string that Google uses to identify the attachment. The destination Google Cloud region and edge availability domain are encoded in the pairing key in the following format:
         
         <random_string>/<region_name>/<domain>
         

The `domain` field contains the string `any` if the VLAN attachment is not restricted to a particular domain or if you don't specify the edge availability domain. For more information about the pairing keys, see [pairing key](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#pairingkey).

  2. Ensure that the edge availability domain of the Partner Interconnect connection matches the domain specified by the pairing key.




### Can't ping Cloud Router (Layer 2 connections)

  * Check that you have the correct VLAN attachment on your on-premises router's subinterface. The VLAN attachment information should match the information provided by your service provider.
  * Check that you have the right IP address on your on-premises router's subinterface. After your service provider configures your VLAN attachment, the attachment allocates a pair of link-local IP addresses. One is for an interface on the associated Cloud Router (`cloudRouterIpAddress`), and the other is for a subinterface on your on-premises router's port channel, not the port channel itself (`customerRouterIpAddress`).
  * If you're testing the performance of your attachments, don't ping Cloud Router. Instead, create and then use a VM in your VPC network. For more information, see Performance testing.



### Loss of optic power on Partner Interconnect connection's port

If there is a loss of optic power on a port, you might encounter one of the following issues:

  * Loss of Layer 3 connectivity (loss of a BGP session) or inability to access your Google Cloud VM instances.
  * Degraded performance of your link bundle. This issue happens if multiple 10GE ports are bundled together and only some of the links in a bundle are functioning.



Loss of optic power on a port means that the hardware is unable to detect a signal from the other end. This can be caused by one of the following issues:

  * A faulty transceiver
  * A faulty transport system
  * A physical fiber issue



To fix this issue, contact your Partner Interconnect and/or circuit provider. They can perform the following steps:

  1. Check that their transceiver is functioning.
  2. Run a hard loop to the Meet-Me Room (MMR) to check if the light levels on their device are working as expected.
  3. Check whether the issues are on their side, or on the Google side. The best way to isolate the interface is to put a bidirectional loop at the demarc. The interfaces on each side will transmit light down to the demarc where it will be looped back to itself. The faulty side will be the side of the demarc that does not come up cleanly.
  4. Clean and reseat all the fiber on their side.



### Can't send and learn MED values over an L3 Partner Interconnect connection

If you are using a Partner Interconnect connection where a Layer 3 service provider handles BGP for you, Cloud Router can't learn MED values from your on-premises router or send MED values to that router. This is because MED values can't pass through autonomous systems. Over this type of connection, you can't set route priorities for routes advertised by Cloud Router to your on-premises router. In addition, you can't set route priorities for routes advertised by your on-premises router to your VPC network.

### IPv6 traffic isn't working after changing an attachment's stack type to dual stack

  1. [View Cloud Router status](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#viewing-router-status) and verify that `status: UP` is displayed.

If BGP isn't up, do the following:

     1. Confirm that your on-premises router (or your partner's router if you are using a Layer 3 partner) is configured with an IPv6 BGP session, and that the session is using the correct IPv6 addresses.

     2. [View the BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration) and verify that `bgpPeers.enable` displays `'TRUE'` for your Cloud Router.

If BGP is up, [view Cloud Router routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#viewing-router-status) to verify that the expected IPv6 `best_routes` are displayed.

If the expected `best_routes` aren't displayed, confirm that your on-premises router (or your partner's router if you are using a Layer 3 partner) is configured with the correct IPv6 routes.




### All other issues

For additional assistance, contact your service provider. If needed, your service provider will contact Google to fix issues related to the Google side of the network.

## HA VPN over Cloud Interconnect

When you deploy HA VPN over Cloud Interconnect, you create two operational tiers:

  * The Cloud Interconnect tier, which includes the VLAN attachments and the Cloud Router for Cloud Interconnect.
  * The HA VPN tier, which includes the HA VPN gateways and tunnels and the Cloud Router for HA VPN.



Each tier requires its own Cloud Router: 

  * The Cloud Router for Cloud Interconnect is used exclusively to exchange VPN gateway prefixes between the VLAN attachments. This Cloud Router is used only by the VLAN attachments of the Cloud Interconnect tier. It cannot be used in the HA VPN tier.
  * The Cloud Router for HA VPN exchanges prefixes between your VPC network and your on-premises network. You configure the Cloud Router for HA VPN and its BGP sessions in the same way you would for a regular HA VPN deployment.



You build the HA VPN tier on top of the Cloud Interconnect tier. Therefore, the HA VPN tier requires that the Cloud Interconnect tier, based on either Dedicated Interconnect or Partner Interconnect, is properly configured and operational.

To troubleshoot an HA VPN over Cloud Interconnect deployment, troubleshoot the Cloud Interconnect tier first. After you verify that Cloud Interconnect is functioning correctly, troubleshoot the HA VPN tier.

### Can't establish BGP session for the Cloud Router for Cloud Interconnect

To detect whether the BGP session associated with the VLAN attachment is down, run the following command:
    
    
       gcloud compute routers get-status INTERCONNECT_ROUTER_NAME
    

Replace `INTERCONNECT_ROUTER_NAME` with the name of the Cloud Router that you created for the Cloud Interconnect tier of your HA VPN over Cloud Interconnect deployment.

To fix this issue, follow these steps:

  1. Follow the steps in [Testing connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/testing-connections) and [Get diagnostics](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/getting-diagnostics) to make sure that the underlying Cloud Interconnect connection is healthy.
  2. Check that the BGP session interface is pointing to the correct attachment.
  3. Check the IP addresses that are configured for the BGP session interface on both the Cloud Router and the on-premises router.
  4. Check that the ASN numbers are correctly configured on both the Cloud Router and the on-premises router.
  5. Check that the Cloud Interconnect connection and the VLAN attachment are in an `admin-enabled` state.



### Can't establish an HA VPN tunnel

To check the tunnel state, run the command:
    
    
    gcloud compute vpn-tunnels describe VPN_TUNNEL_NAME
    

Replace `VPN_TUNNEL_NAME` with the name of the HA VPN tunnel.

To fix this issue, follow these steps:

  1. Because the VPN tunnel is routed over a VLAN attachment, check that the BGP session associated with the VLAN attachment is established. If not, see Can't establish BGP session for the Cloud Router for Cloud Interconnect.
  2. Check whether the tunnel PSK and ciphers are configured correctly on both the Cloud VPN gateways and the on-premises VPN gateways.
  3. Check that the on-premises router's BGP announcement includes the on-premises VPN gateway addresses. If not, adjust the BGP configuration of the on-premises router to advertise the addresses.
  4. Check that the routes to on-premises VPN gateways have not been dropped due to conflicts with existing BGP routes. If there are conflicts, adjust the VPN gateway addresses or advertised routes.
  5. Check that the BGP announcement from Cloud Router includes the HA VPN gateway addresses. Check this from the on-premises router or by inspecting the `advertisedRoutes` field of the BGP peer. To view the `advertisedRoutes` field, run the following command:
         
         gcloud compute routers get-status INTERCONNECT_ROUTER_NAME
         

Replace `INTERCONNECT_ROUTER_NAME` with the name of the Cloud Router that you created for the Cloud Interconnect tier of your HA VPN over Cloud Interconnect deployment.

If the HA VPN gateway addresses are not advertised, ensure that the VLAN attachments are associated with the encrypted Cloud Interconnect router. Check that each VLAN attachment is configured with the expected regional internal IPv4 addresses (`--ipsec-internal-addresses`).




### Can't establish BGP session for the Cloud Router for HA VPN

To check if the BGP session associated with the VLAN attachment is down, run the command:
    
    
    gcloud compute routers get-status VPN_ROUTER_NAME
    

Replace `VPN_ROUTER_NAME` with the name of the Cloud Router that you created for the HA VPN tier of your HA VPN over Cloud Interconnect deployment.

To fix this issue, follow these steps:

  1. Because the BGP traffic is routed over the VPN tunnel, check that the VPN tunnel is established. If not, follow the steps in Can't establish an HA VPN tunnel.
  2. Check that the BGP session interface for the Cloud Router is pointing to the correct VPN tunnel.
  3. Check that the IP addresses of the BGP session interface are configured correctly on both the Cloud Router and the on-premises VPN device.
  4. Check that the ASN numbers are configured correctly on both the Cloud Router and the on-premises router.



### VPC traffic is not reaching on-premises networks or vice versa

The traffic generated from a VM, such as from `ping` or `iperf`, can't reach the on-premises network, or the on-premises network can't reach the traffic generated from a VM.

To fix this issue, follow these steps:

  1. Because the VM traffic is routed over the VPN tunnel, make sure that the route from the VM to the VPN tunnel is being sent by the Cloud Router.

  2. Check that the Cloud Router session for HA VPN is established. If not, see Can't establish BGP session for the Cloud Router for HA VPN.




### Packet loss or low throughput

Traffic from VMs on VPC networks to on-premises networks or traffic from on-premises networks to VPC networks is dropped.

You observe packet loss or low throughput through `ping`, `iperf`, and other network monitoring tools.

To fix this issue, follow these steps:

  1. Check to see if the VLAN attachment is overloaded with traffic. If so, spread the traffic over more VLAN attachments or update the attachment's capacity.
  2. Check whether HA VPN is overloaded with traffic. If so, create additional VPN tunnels over the VLAN attachment to redistribute the traffic.
  3. Make sure that there are no unexpected or sudden spikes in traffic or bursty traffic. TCP streams might be affected by other streams, such as bursty UDP traffic.
  4. Check whether packets exceeding the tunnel MTU are fragmented. Ensure that the MTU is set properly with your VLAN attachments, and check that UDP traffic isn't being MSS clamped.



### VLAN attachment metrics display drops due to `BANDWIDTH_THROTTLE`

When viewing VLAN attachment metrics when you [Monitor connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/monitoring) you may see drops due to `BANDWIDTH_THROTTLE`. This occurs when traffic is being sent at too high of a rate through the attachment, so some traffic is throttled. This is normal behavior, and is usually handled by TCP retransmission.

However, when viewing the corresponding ingress and egress utilization graphs there aren't traffic spikes displayed. This is because the metrics are captured at a 60-second sampling interval, which can mask short traffic spikes or bursts.

If your traffic is throttled rarely, you might not need to address this issue. However, if the bandwidth throttling happens often then you can implement [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff), with jitter in order to avoid synchronized retries from the throttle clients.

### Unable to delete an encrypted VLAN attachment

You receive the following error when you try to delete an encrypted VLAN attachment for Dedicated Interconnect or Partner Interconnect:
    
    
    ResourceInUseByAnotherResourceException
    

To fix this issue, make sure that you have first deleted all the HA VPN gateways and tunnels associated with the encrypted VLAN attachment. For more information, see [Delete HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/delete-ha-vpn-interconnect).

### Mismatched IP address types across encrypted VLAN attachments

When you try to create an HA VPN gateway for use in an HA VPN over Cloud Interconnect deployment, you get the following error:
    
    
    One of the VLAN attachments has private IP address type, while the other one
    has public IP address type; they must have same IP address type.
    

This error occurs when you specify two encrypted VLAN attachments for an HA VPN gateway, and they have different IP addressing schemes for the HA VPN tunnel interfaces. The IP address types must match across both VLAN attachments.

During VPN gateway creation, specify VLAN attachments that use either both private IP addresses or both public IP addresses. If you get this error when creating a VPN gateway, retry recreating the VLAN attachment with the correct address type.

### Missing VLAN attachment from HA VPN gateway interface

If being deployed for HA VPN over Cloud Interconnect, an HA VPN gateway must have an encrypted VLAN attachment specified for both its interfaces.

If you specify only one VLAN attachment, the following error appears:
    
    
    VPN Gateway should have VLAN attachment specified in both interfaces or in none.
    

To fix this issue, create the HA VPN gateway and specify two VLAN attachments.

### Invalid VLAN attachment type

Encrypted VLAN attachments must have the type `DEDICATED` or `PARTNER`.

If you specify an invalid type for an encrypted VLAN attachment, the following error message appears:
    
    
    VLAN attachment should have type DEDICATED or PARTNER.
    

To fix this issue, only create encrypted VLAN attachments with the type `DEDICATED` or `PARTNER`.

### Wrong MTU value for VLAN attachment

When creating an encrypted VLAN attachment for Dedicated Interconnect, the following error message appears:
    
    
    Wrong MTU value [mtuValue] for VLAN attachment.
    The supported MTU for IPsec packets for HA VPN over Cloud Interconnect is 1440.
    

To fix this issue, recreate the attachment with the correct value of `1440`, which is the default value.

### VLAN attachments have a different type

When specifying encrypted VLAN attachments for your HA VPN gateway interfaces, the following error message appears:
    
    
    VLAN attachments should both have same type DEDICATED or PARTNER.
    But found one DEDICATED and one PARTNER.
    

To fix this issue, specify two VLAN attachments that are the same type, either `DEDICATED` or `PARTNER`.

### Dedicated VLAN attachments are not in the same metropolitan area

When specifying encrypted VLAN attachments for your HA VPN gateway interfaces, the following error message appears:
    
    
    Dedicated VLAN attachments should be in the same metropolitan area.
    

To fix this issue, create two encrypted VLAN attachments for Dedicated Interconnect in the same metropolitan area.

### HA VPN gateway is not in the same network as VLAN attachment

When specifying encrypted VLAN attachments for your HA VPN gateway interfaces, the following error message appears:
    
    
    VPN Gateway should be in the same network as VLAN attachment.
    VLAN attachment network: [networkName], VPN gateway network: [networkName]
    

To fix this issue, create the HA VPN gateway in the same network as the encrypted VLAN attachments.

### Wrong encryption type for VLAN attachment

When specifying encrypted VLAN attachments for your HA VPN gateway interfaces, the following error message appears:
    
    
    Wrong encryption type for VLAN attachment [interconnectAttachmentName],
    required IPSEC.
    

To fix this issue, specify only encrypted VLAN attachments that are configured with the encryption type `IPSEC`. If necessary, create encrypted VLAN attachments.

### VLAN attachment zone does not match interfaceId

When specifying encrypted VLAN attachments for your HA VPN gateway interfaces, the following error message appears:
    
    
    VLAN attachment zone should match interfaceId: interface 0 - zone1,
    interface 1 - zone2, but found interface [interfaceId] - [zone] for
    [interconnectAttachmentName].
    

The first HA VPN gateway interface (`interface 0`) must match the encrypted VLAN attachment from zone 1, and the second interface (`interface 1`) must match the encrypted VLAN attachment from zone 2.

To fix this issue, specify encrypted VLAN attachments from the zones matched correctly to the HA VPN gateway interfaces.

### VPN gateway is not in the same region as VLAN attachment

When specifying encrypted VLAN attachments for your HA VPN gateway interfaces, the following error message appears:
    
    
    VPN Gateway should be in the same region as VLAN attachment.
    VLAN attachment region: [region], VPN gateway region: [region].
    

To fix this issue, create HA VPN gateways and encrypted VLAN attachments in the same region.

### Partner VLAN attachment is not in active state

When specifying encrypted VLAN attachments for Partner Interconnect for your HA VPN gateway interfaces, the following error message appears:
    
    
    Interconnect Attachments [name] must be in active state.
    

You must activate the VLAN attachments for Partner Interconnect before you associate them with HA VPN gateway interfaces.

For more information, see [Activate connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/activating-connections).

### Wrong type of Cloud Router specified for VLAN attachment

When you try to create an encrypted VLAN attachment, the following error message appears:
    
    
    Router must be an encrypted interconnect router.
    

To fix this issue, create a Cloud Router with the `--encrypted-interconnect-router` flag. This Cloud Router is used exclusively for HA VPN over Cloud Interconnect.

Then, create the encrypted VLAN attachment and provide the encrypted Cloud Router.

## Cross-Cloud Interconnect

This section describes issues that can come up with Cross-Cloud Interconnect.

Google supports the connection up to the point where it reaches the network of your other cloud service provider. Google does not guarantee uptime from the other cloud service provider and cannot create a support ticket on your behalf. With your permission [Customer Care](https://docs.cloud.google.com/support) can communicate directly with your other cloud provider's support team to expedite issue resolution. However, you must have a support ticket open with the other provider.

### Mismatches between redundant ports

After you order Cross-Cloud Interconnect ports, you give Google information about how you want the ports connected to your remote cloud ports. You also use this information later, when you configure your resources. If you have connectivity issues, one problem might be that you didn't use the correct connectivity details.

For example, you might provide instructions like the following:

  * Connect `gcp-1` to `azure-1`.

  * Connect `gcp-2` to `azure-2`.




However, when configuring your resources, you might assume that the ports are connected as follows:

  * Connect `gcp-1` to `azure-2`.

  * Connect `gcp-2` to `azure-1`.




This condition might be detectable through examination of the ARP cache. However, a simpler solution is to go to the remote cloud and try swapping the IP address ranges assigned to the two BGP peers.

For example, suppose `azure-1` has a VLAN attachment peering on 169.254.0.2 and `azure-2` has a VLAN attachment peering on 169.254.99.2. Swap the IP address ranges so that the `azure-1` attachment uses 169.254.99.2 and the `azure-2` attachment uses 169.254.0.2.

If you used different VLAN IDs for the attachment on each port, you would also need to swap the VLAN IDs used by the attachments. For Azure, this scenario is impossible because it requires using the same VLAN ID on both ports for each attachment.

### VLAN IDs

Sometimes connectivity problems can be traced to mistakes with VLAN ID values. VLAN ID is a field on your Cross-Cloud Interconnect VLAN attachment.

#### Azure

Azure requires that VLAN IDs be allocated identically on both ports of a pair. When you create your VLAN attachment, the Google Cloud console enforces this requirement. However, if you set up the attachments by using the Google Cloud CLI or the API, it's possible to allocate different VLAN IDs. This risk is especially great if you let VLAN IDs be automatically assigned when you create the attachment. If you don't explicitly set the ID, it's automatically assigned.

#### AWS

When connecting to AWS, it's OK to use automatic assignment of VLAN IDs. However, when configuring your AWS resources, you must manually configure the VLAN IDs to match the ones that Google Cloud automatically assigned. Also, it's important to not confuse which VLAN ID should be used for each port. If the wrong VLAN ID is configured on a port, the virtual routers are unable to communicate.

### Verify connectivity

If you haven't already, follow the steps for verifying connectivity between Google Cloud and your remote cloud network:

  * [Verify your connection (AWS)](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/test-connections)
  * [Verify your connection (Azure)](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/test-connections)
  * [Verify your connection (OCI)](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/test-connections)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
