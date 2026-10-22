---
url: https://docs.cloud.google.com/nat/docs/troubleshooting/
title: Troubleshoot configuration \u00a0|\u00a0 Cloud NAT \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:41.685451+00:00
---

# Troubleshoot configuration  |  Cloud NAT  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nat/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NAT ](https://docs.cloud.google.com/nat/docs)
  * [ Guides ](https://docs.cloud.google.com/nat/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot configuration

This guide can help you solve common issues with Cloud NAT.

## Common issues

### VMs can reach the internet unexpectedly, without Cloud NAT

If your virtual machine (VM) instances or container instances can reach the internet without Cloud NAT, but you don't want them to, check for the following issues:

  * Determine if the VM's network interface has an external IP address. If the network interface has an external IP address assigned to it, Google Cloud automatically performs one-to-one NAT for packets whose sources match the interface's primary internal IP address. For more information, see [Cloud NAT specifications](https://docs.cloud.google.com/nat/docs/overview#specifications).

To determine if a VM has an external IP address, see [changing or assigning an external IP address to an existing instance](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#IP_assign).

  * Ensure that your Google Kubernetes Engine (GKE) cluster is a [private cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters). Each node VM in a non-private cluster has an external IP address, so each node can use routes in your Virtual Private Cloud (VPC) network whose next hop is the default internet gateway without relying on Cloud NAT. For more information, including how non-private clusters interact with Cloud NAT gateways, see [Compute Engine interaction](https://docs.cloud.google.com/nat/docs/overview#NATwithGKE).

  * [List routes](https://docs.cloud.google.com/vpc/docs/using-routes#listingroutes) in your Virtual Private Cloud network, looking for ones that could provide internet connectivity through a next hop different than the default internet gateway. As examples:

    * [Static routes](https://docs.cloud.google.com/vpc/docs/static-routes) whose next hops are VMs, internal passthrough Network Load Balancers, or Cloud VPN tunnels might indirectly provide internet connectivity. For example, the next hop VMs or backend VMs for an internal passthrough Network Load Balancer might have external IP addresses themselves, or a Cloud VPN tunnel might connect to a network that offers internet access.

    * [Dynamic routes](https://docs.cloud.google.com/vpc/docs/routes#dynamic_routes) learned from on-premises networks by Cloud Routers in your VPC network might connect to a network that offers internet access.

  * Keep in mind that other custom routes in your VPC network might have higher priorities than routes whose next hops are default internet gateways. For information about how Google Cloud evaluates routes, see routing [applicability and order](https://docs.cloud.google.com/vpc/docs/routes#instancerouting).




### No logs are generated

  * [Verify that NAT logging is enabled](https://docs.cloud.google.com/nat/docs/monitoring#logging-status).
  * Double-check that your view of the logs isn't filtering out the logs that you are looking for. For instructions, see [Viewing logs](https://docs.cloud.google.com/nat/docs/monitoring#viewing-logs).

  * Make sure that a firewall rule isn't blocking traffic. Firewall rules that block egress (outbound) traffic are applied before the traffic would have been sent to the NAT gateway. You can use [Firewall Rules Logging](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging) to see if your custom egress rules are blocking outbound traffic.

  * Review [Types of Cloud NAT](https://docs.cloud.google.com/nat/docs/overview#nat_types). The destination for your traffic might not be handled by NAT.




### Certain logs are excluded

  * [Verify that NAT logging is enabled](https://docs.cloud.google.com/nat/docs/monitoring#logging-status) and that your log filter is not excluding logs that you want to keep. You can [clear a logs filter](https://docs.cloud.google.com/nat/docs/monitoring#clear-logs-filter) so that nothing is excluded.

  * Cloud NAT does not log every single event. During periods of heavy egress traffic, NAT logging is throttled, proportional to the machine type of the VM. Translation or error logs might be dropped, and it is not possible to determine what is omitted during throttling.




### Packets dropped with reason: out of resources

If you see packet loss from VMs that use Cloud NAT, this might be because there are not enough available NAT source IP address and source port tuples for the VM to use at the time of the packet loss (port exhaustion). A five-tuple (NAT source IP address, source port, and destination 3-tuple) cannot be reused within the [TCP TIME_WAIT timeout](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#nat-timeouts).

If there aren't enough available NAT tuples, the `dropped_sent_packets_count` [reason](https://docs.cloud.google.com/nat/docs/monitoring#vm_instance_filtering_dimensions) is `OUT_OF_RESOURCES`. For more information about metrics, see [Using VM instance metrics](https://docs.cloud.google.com/nat/docs/monitoring#monitoring).

See Reduce your port usage for ways to reduce port usage.

If you use dynamic port allocation, see the following section for ways to reduce packet drops when dynamic port allocation is used.

#### Packets dropped when dynamic port allocation is configured

Dynamic port allocation detects when a VM is close to being out of ports, and doubles the number of ports that are allocated to the VM. This helps ensure that ports aren't wasted, but can result in dropped packets while the number of allocated ports is increasing.

To reduce the number of dropped packets, consider the following:

  * If you can ramp up connections more slowly, Cloud NAT has more time to allocate more ports.

  * If VMs are making TCP connections, you can configure the VMs with a larger value for `tcp_syn_retries`, which gives the system more time to establish the connection and increases the chances for the connection to succeed.

For example, for Linux VMs, you can view the current setting:
        
        sysctl net.ipv4.tcp_syn_retries
          

If needed you can increase the setting:
        
        sudo sysctl -w net.ipv4.tcp_syn_retries=NUM
          

**Note:** Increasing the value for `tcp_syn_retries` can lead to latency because the system keeps dropping packets until the connection succeeds after multiple retries.
  * If you have bursty workloads and need to quickly allocate more ports, you might need to adjust the minimum number of ports per VM. [View your port usage](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#view-port-usage) and [determine an appropriate minimum number of ports per VM](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#choose-minimum).




### Packets dropped with reason: endpoint independence conflict

**Note:** This section doesn't apply to Private NAT.

If you see packet loss from VMs that use Public NAT, and you have endpoint-independent mapping (EIM) turned on, the packet loss might be caused by an [endpoint independent conflict](https://docs.cloud.google.com/nat/docs/ports-and-addresses#ports-reuse-endpoints). If it is, the `dropped_sent_packets_count` [reason](https://docs.cloud.google.com/nat/docs/monitoring#vm_instance_filtering_dimensions) is `ENDPOINT_INDEPENDENCE_CONFLICT`. For more information about metrics, see [Using VM instance metrics](https://docs.cloud.google.com/nat/docs/monitoring#monitoring).

You can reduce the chances of endpoint independent conflicts by using the following techniques:

  * [Turn off endpoint-independent mapping](https://docs.cloud.google.com/nat/docs/set-up-network-address-translation#set-mapping). This allows the new connection from a given source IP address and port to use a different NAT source IP address and port than it used before. Disabling or enabling endpoint-independent mapping does not interrupt established connections.

  * [Increase the minimum default number of NAT ports per VM instance](https://docs.cloud.google.com/nat/docs/set-up-network-address-translation#change_minimum_default_ports_allocated_per_vm_associated_with_nat), so that the [port reservation procedure](https://docs.cloud.google.com/nat/docs/ports-and-addresses#port-reservation-procedure) can assign more NAT source IP address and source port tuples to each client VM. This decreases the probability that two or more client IP address and ephemeral source port tuples are assigned the same NAT source IP address and source port tuple.

  * Check how many ephemeral source ports are being used:

    * For Linux VMs:
          
          netstat -an | egrep 'ESTABLISHED|TIME_WAIT|CLOSE_WAIT' | wc -l
          

    * For Windows VMs:
          
          netstat -tan | findstr "ESTABLISHED TIME_WAIT CLOSE_WAIT" | find /c /v ""
          

  * Configure your VM instances to use a larger set of ephemeral source ports:

    * For Linux VMs:

      * You can view what port range is configured with this command:
            
            cat /proc/sys/net/ipv4/ip_local_port_range
            

      * You can set the `ip_local_port_range` to the maximum number of ephemeral source ports (64,512) with this command:
            
            echo 1024 65535 > /proc/sys/net/ipv4/ip_local_port_range
            

    * For Windows VMs:

      * You can view what port ranges are configured with these commands:
            
            netsh int ipv4 show dynamicport tcp
            netsh int ipv4 show dynamicport udp
            

      * You can set the number of ephemeral source TCP and UDP ports to the maximum possible (64,512) with these commands:
            
            netsh int ipv4 set dynamicport **tcp** start=1024 num=64512
            netsh int ipv4 set dynamicport **udp** start=1024 num=64512
            

      * On Google Kubernetes Engine nodes, you can automate this configuration by using a privileged `DaemonSet`.

  * For GKE clusters, disable the source NAT performed on each node for packets sent to destinations of interest. You can do this in one of two ways:

    * By deploying the [`ip-masq-agent`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent) and adding the destinations of interest to the list of `nonMasqueradeCIDRs`.

    * By disabling SNAT for the [default non-masquerade destinations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent#default-non-masq-dests) with the [`--disable-default-snat` flag](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/clusters/create#--disable-default-snat) when you create a cluster.




### Dropped received packets

A Cloud NAT gateway maintains a connection tracking table to store active connection details and mappings of VM IP addresses and ports to NAT IP addresses and ports. A Cloud NAT gateway drops an ingress packet if the connection tracking table doesn't contain any entry for the connection.

A connection entry might be missing due to any of the following reasons:

  * An established TCP connection timed out because the TCP Established Connection Idle Timeout expired.
  * An external endpoint failed to respond to the connection request before the TCP Transitory Connection Idle Timeout expired. For example, a Google Cloud resource initiated a connection with a `SYN`, but the external endpoint failed to respond with a `SYN-ACK`.
  * Cloud NAT doesn't accept unsolicited inbound connections. These packets don't match any entries in the connection tracking table and are dropped.
  * Modifying Cloud NAT configurations can disrupt existing connections. Specifically, if you don't [drain external IP addresses](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation#draining) before [removing](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation#change_external_ip_addresses_associated_with_nat) them, any connections that use those addresses are immediately removed from the connection tracking table and all return traffic is dropped.

To see which other configuration changes cause connection drops, refer to [Impact of tuning NAT configurations on existing NAT connections](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#impact-nat-tuning-existing-conns).




#### Address application impact

Before troubleshooting, confirm whether ingress packet drops are affecting your application by checking for application errors that coincide with spikes in dropped ingress packets. If the application is impacted, use one or more of the following methods to address the issue:

  * Use keepalive mechanisms in your application so that long-running connections can stay open for a longer period.
  * Increase the TCP Transitory Connection Idle Timeout to provide external endpoints additional time to respond to Google Cloud resources so that the connection can be established.
  * Increase the TCP Established Connection Idle Timeout if you have significantly decreased the default value.

**Note:** Increasing the TCP Transitory Connection Idle Timeout or TCP Established Connection Idle Timeout delays port reuse because the Cloud NAT gateway keeps the mapping between a specific port and a connection for a longer period, even for unestablished or inactive connections.

### Need to allocate more IP addresses

Sometimes your VMs are unable to reach the internet because you don't have enough [NAT IP addresses](https://docs.cloud.google.com/nat/docs/ports-and-addresses#addresses). Multiple factors can cause this problem. For more information, see the following table.

Root cause | Symptom | Solution  
---|---|---  
You've manually allocated addresses, but you haven't allocated enough of them, given your current port usage.  | 

  * The Google Cloud console displays an error that reads _You need to allocate at least 'X' more IP addresses to allow all instances to access the internet_. 
  * The value of the [`nat_allocation_failed`](https://docs.cloud.google.com/nat/docs/monitoring#gateway-metrics) metric is `true`. 

| Do one of the following:

  * Minimize your port usage, as described in Reduce your port usage.
  * Manually add more IP addresses, as described in [Update external IP addresses associated with NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation#change_external_ip_addresses_associated_with_nat).

  
You have surpassed a [hard limit](https://docs.cloud.google.com/nat/quota#limits) for NAT IP addresses.  | 

  * The value of the [`nat_allocation_failed`](https://docs.cloud.google.com/nat/docs/monitoring#gateway-metrics) metric is `true`. 

| 

  * Minimize your port usage, as described in Reduce your port usage.

  
  
To monitor failures caused by an insufficient number of IP addresses, create an alert for the [`nat_allocation_failed`](https://docs.cloud.google.com/nat/docs/monitoring#gateway-metrics) metric. This metric is set to `true` if Google Cloud is unable to allocate sufficient IP addresses for any VM in your NAT gateway. For information about alert policies, see [Defining alerting policies.](https://docs.cloud.google.com/nat/docs/monitoring#defining_alerting_policies)

### Reduce your port usage

You can minimize the number of ports that each VM uses in situations where allocating more NAT IP addresses is not possible or desirable.

**Important:** If you need endpoint-independent mapping, the recommendations in this section don't apply. You must increase the number of available NAT IP address and port tuples configured on the NAT gateway or use multiple NAT gateways.**Warning:** Established connections may be interrupted if you enable or disable dynamic port allocation, or if you decrease the minimum number of ports per VM. For more information, see [Switch port allocation method](https://docs.cloud.google.com/nat/docs/ports-and-addresses#switch-port-allocation) and [Reduce ports per VM](https://docs.cloud.google.com/nat/docs/ports-and-addresses#specs-reducing).

To reduce port usage, complete the following steps:

  1. Disable [Endpoint-Independent Mapping](https://docs.cloud.google.com/nat/docs/ports-and-addresses#ports-reuse-endpoints).

  2. Enable [dynamic port allocation](https://docs.cloud.google.com/nat/docs/ports-and-addresses#dynamic-port). To use dynamic port allocation, you set a minimum number of ports per VM and a maximum number of ports per VM. Cloud NAT automatically allocates a number of NAT source IP address and source port tuples between the minimum and maximum number of ports, inclusive. Using a low number for the minimum number of ports reduces wasting NAT source IP address and source port tuples on VMs with fewer active connections. If you encounter connection timeouts while ports are being allocated, see Reduce packet drops with dynamic port allocation.

  3. Determine the lowest possible minimum number of ports to meet your needs. There are several methods to do this, and most rely on reviewing the number of used ports (`compute.googleapis.com/nat/port_usage`) as input to the decision-making process. For information about how to find port usage, see [View port usage](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#view-port-usage). The following are two example methods to determine a minimum number of ports:

     * Consider the average value of `compute.googleapis.com/nat/port_usage` over a representative time period for a representative number of VMs.
     * Consider the most frequently occurring value of `compute.googleapis.com/nat/port_usage` over a representative time period for a representative number of VMs.
  4. Determine the lowest possible maximum number of ports to meet your needs. Once again, review `compute.googleapis.com/nat/port_usage` as input to your decision-making process. Consider the maximum value of `compute.googleapis.com/nat/port_usage` over a representative time period for a representative number of VMs as a starting point for the maximum number of ports. Keep in mind that setting the maximum number too high can prevent other VMs from receiving NAT source IP address and source port tuples.

  5. Finding the right values for minimum and maximum ports involves iterative testing. For steps to change minimum and maximum port numbers, see [Change minimum or maximum ports when dynamic port allocation is configured](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#change-dynamic-port).

  6. Review the [NAT timeouts](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#nat-timeouts), their meanings, and their default values. If you need to rapidly create a series of TCP connections to the same destination 3-tuple, consider reducing the TCP time wait so that Cloud NAT can more quickly re-use NAT source IP address and source port tuples. This allows Cloud NAT to more quickly use the same 5-tuple instead of needing to use a unique 5-tuple, which might require allocation of additional NAT source IP address and source port tuples for each sending VM. For steps to change NAT timeouts, see [Change NAT timeouts](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#change-conn-timeout).




## Frequently asked questions

### Regional restriction for Cloud NAT

#### Can I use the same Cloud NAT gateway in more than one region?

No. A Cloud NAT gateway cannot be associated with more than one region, VPC network, or Cloud Router.

If you need to provide connectivity for other regions or VPC networks, create additional Cloud NAT gateways for them.

#### Are the external NAT IP addresses used by Cloud NAT gateways global or regional?

Cloud NAT gateways use _regional external IP addresses_ as NAT IP addresses. Even though they are regional, they are publicly routable. For information about different ways that NAT IP addresses can be allocated or assigned, see [NAT IP addresses](https://docs.cloud.google.com/nat/docs/ports-and-addresses#addresses).

### When Cloud NAT can and cannot be used

#### Does Cloud NAT apply to instances, including GKE node VMs, that have external IP addresses?

Generally, no. If the network interface of a VM has an external IP address, Google Cloud always performs 1-to-1 NAT for packets sent from the primary internal IP address of the network interface without using Cloud NAT. However, Cloud NAT could still provide NAT services to packets sent from alias IP address ranges of that same network interface. For additional details, see [Cloud NAT specifications](https://docs.cloud.google.com/nat/docs/overview#specifications) and [Compute Engine interaction](https://docs.cloud.google.com/nat/docs/overview#NATwithGKE).

#### Does Public NAT let a source VM whose network interface lacks an external IP address send traffic to a destination VM or load balancer that has an external IP address, even when the source and destination are in the same VPC network?

Yes. The network path involves sending traffic out of the VPC network through a default internet gateway, and then receiving it in the same network.

When the source VM sends a packet to the destination, Public NAT performs source NAT (SNAT) before delivering the packet to the second instance. Public NAT performs destination NAT (DNAT) for responses from the second instance to the first. For a step-by-step example, see [Basic Public NAT configuration and workflow](https://docs.cloud.google.com/nat/docs/public-nat#snat-flow-example).

#### Can I use Private NAT for communication between VMs in the same VPC network?

No, Private NAT doesn't perform NAT on traffic between VMs in the same VPC network.

### Unsolicited incoming connections not supported

#### Does Cloud NAT allow for inbound connections (for example, SSH) to instances without external IP addresses?

No, Cloud NAT does not support _unsolicited_ incoming connections. For more information, see [Cloud NAT specifications](https://docs.cloud.google.com/nat/docs/overview#specifications). However, Google Cloud's network edge might respond to pings if the destination IP address is a Cloud NAT gateway external IP address that has active port mappings to at least one VM instance. To see IP addresses assigned to a Cloud NAT gateway, use the [gcloud compute routers get-nat-ip-info command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/get-nat-ip-info). External IP addresses marked as `IN_USE` might respond to pings.

If you need to connect to a VM that doesn't have an external IP address, see [Choose a connection option for internal-only VMs](https://docs.cloud.google.com/compute/docs/connect/ssh-internal-ip). For example, as part of the [Cloud NAT example Compute Engine setup](https://docs.cloud.google.com/nat/docs/gce-example), you connect to a VM without an external IP address by using Identity-Aware Proxy.

### Cloud NAT and ports

#### Why does a VM have a fixed number of ports (`64` by default)?

When a Cloud NAT gateway provides NAT for a VM, it reserves source address and source port tuples according to the [port reservation procedure](https://docs.cloud.google.com/nat/docs/ports-and-addresses#port-reservation-procedure).

For more information, see [port reservation examples](https://docs.cloud.google.com/nat/docs/ports-and-addresses#port-reservation-examples).

#### Can I change the minimum number of ports reserved for a VM?

Yes. You can increase or decrease the minimum number of ports per VM when you create a new Cloud NAT gateway or by editing it later. Each Cloud NAT gateway reserves source address and source port tuples according to the [port reservation procedure](https://docs.cloud.google.com/nat/docs/ports-and-addresses#port-reservation-procedure).

For additional information about _decreasing_ the minimum number of ports, see the next question.

#### Can I decrease the minimum number of ports per VM after creating the Cloud NAT gateway?

Yes; however, decreasing the minimum number of ports could result in the [port reservation procedure](https://docs.cloud.google.com/nat/docs/ports-and-addresses#port-reservation-procedure) reserving a smaller number of ports per VM. When this happens, existing TCP connections might be reset and, if so, must be re-established.

#### When switching NAT mapping from Primary and Secondary ranges to Primary range only, are additional ports allocated to each instance immediately released?

No. Any additional ports used by secondary ranges are retained by instances until the **minimum ports per VM** setting is reduced. When Cloud NAT is configured to map Secondary (alias) ranges for subnets, Cloud NAT assigns a minimum of 1,024 ports per instance, based on the [port reservation procedure](https://docs.cloud.google.com/nat/docs/ports-and-addresses#port-reservation-procedure).

By switching to Primary ranges only, Cloud NAT conserves those additional allocated ports for instances that have already had those ports assigned. After changing the ranges for which Cloud NAT is applied to Primary only, the actual number of ports assigned to those instances is not changed until the **minimum ports per VM** setting is also reduced.

To reduce the amount of ports allocated to those instances, after switching to primary ranges, the **minimum ports per VM** setting must be reduced. After that value is reduced, Cloud NAT automatically adjusts the number of ports allocated per instance down, which reduces port consumption.

### Cloud NAT and other Google services

#### Does Cloud NAT enable access to Google APIs and services?

When you enable Cloud NAT for a subnet's primary IP range, Google Cloud automatically enables [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access). For more information, see [Private Google Access interaction](https://docs.cloud.google.com/nat/docs/overview#interaction-pga).

## Investigate Cloud NAT issues with Gemini Cloud Assist

You can use [Gemini Cloud Assist investigations](https://docs.cloud.google.com/gemini/docs/cloud-assist/investigations) to troubleshoot Cloud NAT issues.

To create an investigation, do the following:

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click your Cloud NAT gateway.

  3. On the **Cloud NAT gateway details** page, click auto_awesome**Investigate**.

  4. In the investigation creation panel, describe the issue that you want to troubleshoot, select the affected resources, and then click **Create** to start the investigation.

For more information, see [Create an investigation](https://docs.cloud.google.com/gemini/docs/cloud-assist/create-investigation#create).




For warnings and errors in your Cloud NAT configuration, the **Investigate** button is displayed with the alert. When creating an investigation for a warning or error, an issue description and relevant resources are automatically pre-populated into the investigation creation panel.

## What's next

  * [Getting support](https://docs.cloud.google.com/nat/docs/getting-support)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
