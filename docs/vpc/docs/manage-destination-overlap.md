---
url: https://docs.cloud.google.com/vpc/docs/manage-destination-overlap/
title: Manage destination overlap \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:53.148941+00:00
---

# Manage destination overlap  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/manage-destination-overlap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage destination overlap

This page describes how producer network administrators can manage destination overlap in a Virtual Private Cloud (VPC) network that uses a Private Service Connect interface.

Google Cloud ensures that the IP address ranges of subnets that are assigned to network interfaces on the same virtual machine (VM) instance can't have overlapping IP address ranges. However, subnets in the consumer and producer VPC networks can overlap, as shown in figure 1. When using a Private Service Connect interface with overlapping destination IP address ranges, additional configuration is necessary to ensure that traffic reaches the correct destination in the intended network.

The commands described on this page show how to temporarily update routing for a VM that uses the Debian operating system. To permanently update the VM, or to configure a VM that has a different operating system, consult the operating system's public documentation.

[ ![](https://docs.cloud.google.com/static/vpc/images/psc-interfaces/destination-overlap.svg)](https://docs.cloud.google.com/static/vpc/images/psc-interfaces/destination-overlap.svg) `Subnet-a` in a producer VPC network overlaps with `subnet-c` in a consumer VPC network because both subnets use the same IP address range. A producer VM needs to be able to reach `10.0.1.5` in both networks.

You can manage overlapping destination IP address ranges in the following ways, which are described in detail on this page:

  * [Use network namespaces](https://docs.cloud.google.com/vpc/docs/manage-destination-overlap#overlap-namespaces) to create separate routing tables for each application.
  * [Apply policy-based routing](https://docs.cloud.google.com/vpc/docs/manage-destination-overlap#overlap-pbr) to your interface's VM to direct traffic based on target ports.



The following approaches can also be used to manage destination overlap, but they are not described on this page:

  * Use a socket library and [`bind()`](https://man7.org/linux/man-pages/man2/bind.2.html) to control routing.
  * Use a completely non-overlapping IP address space for the producer network.
  * If the overlapping IP addresses on the producer side are only for first-party API endpoints, you can [Configure Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid).
  * Use [virtual routing and forwarding (VRF)](https://en.wikipedia.org/wiki/Virtual_routing_and_forwarding) to isolate overlapping IP address spaces. Assign a VRF instance to each Private Service Connect interface. Configure default routes for each VRF instance to ensure that traffic reaches the intended destination.
  * Use [eBPF](https://ebpf.io/what-is-ebpf/) to customize advanced routing rules based on criteria other than IP address. This approach is recommended for cases where the previous options are not feasible.



### Manage destination address overlap by using network namespaces

You can manage destination address overlap by using network namespaces. This approach works well when some applications on a producer VM only need to access consumer workloads, and other applications on the producer VM only need to access producer workloads.

To manage destination address overlap by using network namespaces, do the following:

  1. [Connect](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms) to the VM that has your Private Service Connect interface. 

  2. [Find the guest OS name](https://docs.cloud.google.com/vpc/docs/configure-routing-private-service-connect-interfaces#find-os-interface-name) of your Private Service Connect interface.

  3. To create a network namespace for consumer-bound traffic, use the following command:
         
         sudo ip netns add consumer-ns
         

  4. Move the Private Service Connect interface to the consumer network namespace. Run the following commands individually:
         
         sudo ip link set OS_INTERFACE_NAME netns consumer-ns
         
         
         sudo ip netns exec consumer-ns ip link set OS_INTERFACE_NAME up
         

Replace `OS_INTERFACE_NAME` with the guest OS name for your Private Service Connect interface that you found in a previous step.

  5. Restore the Private Service Connect interface's IP address:
         
         sudo ip netns exec consumer-ns ip addr add INTERFACE_IP/32 dev OS_INTERFACE_NAME
         

Replace `INTERFACE_IP` with the IP address of your Private Service Connect interface.

  6. Validate the changes to your Private Service Connect interface:
         
         sudo ip netns exec consumer-ns ip a
         

Verify that the guest OS name of your Private Service Connect interface is listed in the command's output. Verify that the interface has the correct IP address.

  7. Add a route to the gateway IP address:
         
         sudo ip netns exec consumer-ns ip route add GATEWAY_IP dev OS_INTERFACE_NAME scope link
         

Replace `GATEWAY_IP` with the [IP address of the default gateway](https://docs.cloud.google.com/vpc/docs/configure-routing-private-service-connect-interfaces#find-default-gateway-ip) for your Private Service Connect interface's subnet.

  8. Add a default route for your Private Service Connect interface:
         
         sudo ip netns exec consumer-ns ip route add default via GATEWAY_IP dev OS_INTERFACE_NAME
         

  9. Validate the routing table for the `consumer-ns` namespace:
         
         sudo ip netns exec consumer-ns ip route
         

Make sure that the routing table has an entry of the following form:
         
         default via GATEWAY_IP dev OS_INTERFACE_NAME
         

  10. To verify that your interface can reach VMs in each part of the overlapping IP address range, do the following:

     1. Make sure that firewall rules are [configured to allow ingress `ICMP` traffic](https://docs.cloud.google.com/firewall/docs/using-firewalls#common-use-cases-allow-icmp) to your target VMs.

     2. Send an `ICMP` ping from your interface's VM to a consumer VM that's in the overlapping IP address range. Use your consumer namespace:
            
            sudo ip netns exec consumer-ns ping CONSUMER_IP_ADDRESS
            

Replace `CONSUMER_IP_ADDRESS` with the IP address of a consumer VM from the overlapping IP address range.

     3. Send an `ICMP` ping from your interface's VM to a producer VM that's in the overlapping IP address range. Use the default namespace:
            
            ping PRODUCER_IP_ADDRESS
            

Replace `PRODUCER_IP_ADDRESS` with the IP address of a producer VM from the overlapping IP address range.




### Manage destination address overlap with policy-based routing

You can manage destination address overlap by configuring policy-based routing on the operating system of your interface's VM. This approach works well when the same application needs to access workloads that are in both the consumer and producer VPC networks, but you must repeat the procedure for each different port that you want to reach in the overlapping IP range.

When you set up policy-based routing to manage destination overlap, you choose target ports to use for consumer applications. Traffic that's bound for one of these ports flows through your Private Service Connect interface to the consumer subnet, while other traffic flows through the default interface to the producer subnet.

  1. [Connect](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms) to your Private Service Connect interface's VM.

  2. If the `iproute2` command is not available, install it.

  3. Ensure that you can write to the following file: `/etc/iproute2/rt_tables`

  4. Create a route table. Add a default route for your Private Service Connect interface:
         
         echo "200 pscnet" >> /etc/iproute2/rt_tables \
         sudo ip route add default dev OS_INTERFACE_NAME table pscnet
         

Replace `OS_INTERFACE_NAME` with the [guest OS name of your Private Service Connect interface](https://docs.cloud.google.com/vpc/docs/configure-routing-private-service-connect-interfaces#find-os-interface-name)—for example, `ens5`.

  5. Add a route to the overlapping consumer subnet range through your default gateway:
         
         sudo ip route add CONSUMER_SUBNET_RANGE via GATEWAY_IP dev OS_INTERFACE_NAME table pscnet
         

Replace the following:

     * `CONSUMER_SUBNET_RANGE`: the IP address range of your consumer subnet.
     * `GATEWAY_IP`: the [IP address of the default gateway](https://docs.cloud.google.com/vpc/docs/configure-routing-private-service-connect-interfaces#find-default-gateway-ip) for your Private Service Connect interface's subnet.
  6. Update the route table so that egress packets from this VM use your interface's IP address as their source IP address:
         
         sudo ip route add GATEWAY_IP src INTERFACE_IP dev OS_INTERFACE_NAME table pscnet
         

Replace `INTERFACE_IP` with the IP address of your Private Service Connect interface.

  7. Add an IP rule that applies to all traffic that's destined for the target port of your consumer application:
         
         sudo ip rule add dport CONSUMER_PORT table pscnet
         

Replace `CONSUMER_PORT` with the port that you have configured for traffic to your consumer VM.

  8. To verify that a packet is routed to the correct VM based on its destination port, do the following:

     1. Create test VMs in the producer and consumer networks that both use the same IP address from the overlapping range.
     2. Set up an HTTP server on each test VM. Configure the consumer test VM to listen on the port that you've set up for the consumer application. Configure the producer test VM to listen on a port that's different from the one you've set up for the consumer application.
     3. Ensure that [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) are configured to allow HTTP traffic to your test VMs.
     4. Using the port that you've configured for your consumer application, make a `GET` request to the test IP address, and then verify that you've reached the correct instance:
            
            curl TEST_IP_ADDRESS:CONSUMER_PORT
            

Replace the following:

        * `TEST_IP_ADDRESS`: the IP address of your test VMs.
        * `CONSUMER_PORT`: the port of your consumer application.
     5. Using the port that you've configured for your production test VM, make a `GET` request to the test IP address, and then verify that you've reached the correct instance:
            
            curl IP_ADDRESS:PRODUCER_PORT
            

Replace the following:

        * `IP_ADDRESS`: the IP address of your test VMs.
        * `PRODUCER_PORT`: the port that you've configured for your production test VM.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
