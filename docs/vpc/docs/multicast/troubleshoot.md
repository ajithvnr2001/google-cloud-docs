---
url: https://docs.cloud.google.com/vpc/docs/multicast/troubleshoot/
title: Troubleshoot Cloud Multicast \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:50.107974+00:00
---

# Troubleshoot Cloud Multicast  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Cloud Multicast ](https://docs.cloud.google.com/vpc/docs/multicast)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/multicast/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot Cloud Multicast

**GA with allowlist:** Access to Cloud Multicast is available to select Google Cloud customers. If you are interested, submit an [access request form](https://forms.gle/G6o6wXTBqijoEHs26). 

This page provides troubleshooting information for Cloud Multicast.

For information about monitoring multicast traffic, see [Observability for Cloud Multicast](https://docs.cloud.google.com/vpc/docs/multicast/observability).

## Example commands for testing multicast traffic

This section provides example commands for testing multicast traffic by using the [`iperf` tool](https://wikipedia.org/wiki/Iperf). To run these example commands, you must set up the multicast configuration described in the [Cloud Multicast configuration overview](https://docs.cloud.google.com/vpc/docs/multicast/configuration-overview).

**Note:** The example commands in this section use the `iperf` tool. If your VM instance doesn't have an external IP address, then you must configure [Cloud NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation) so that you can install the `iperf` package on the instance.

### Send multicast traffic from a multicast producer

  1. [Connect to the instance](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms) by using SSH.

  2. Install `iperf` if you haven't already.
         
         sudo apt install iperf
         

  3. To send multicast traffic to the multicast group IP address, run the following command:
         
         iperf -c MULTICAST_GROUP_ADDRESS -p 1234 -l 1500 -i 1 -u -b 1000pps -t 999999
         

Replace `MULTICAST_GROUP_ADDRESS` with the multicast group IP address.




### Join a group and receive multicast traffic from a multicast consumer

  1. [Connect to the instance](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms) by using SSH.

  2. Install `iperf` if you haven't already.
         
         sudo apt install iperf
         

  3. To join a multicast group and log the traffic that you receive, run the following command:
         
         iperf -s -p 1234 -B MULTICAST_GROUP_ADDRESS -l 1500 -u -i 1
         

Replace `MULTICAST_GROUP_ADDRESS` with the multicast group IP address.

For example, the following command joins a group with the IP address `224.1.0.176` to receive packets up to 1500 bytes and logs the traffic received:
         
         iperf -s -p 1234 -B 224.1.0.176 -l 1500 -u -i 1
         




## Troubleshoot specific issues

The following sections describe how to troubleshoot specific issues that you might encounter when using Cloud Multicast.

### Creating a multicast producer configuration fails

This section describes an error that might occur when attempting to create multicast producer and consumer configurations in the same VPC network.

If you complete the steps to [enable a VPC network to consume multicast traffic](https://docs.cloud.google.com/vpc/docs/multicast/enable-consumer-network#enable-network) before completing the corresponding steps to [enable a VPC network to produce multicast traffic](https://docs.cloud.google.com/vpc/docs/multicast/enable-producer-network#enable-network), then you receive an error similar to the following when attempting to complete the multicast producer configuration:
    
    
    The request was invalid: MulticastProducerAssociation cannot be created in the
    same network as MulticastConsumerAssociation. Please delete 
    MulticastConsumerAssociation projects/PROJECT_ID/locations/ZONE/multicastConsumerAssociations/CONSUMER_ASSOCIATION_NAME
    first.
    

To resolve this issue, do the following:

  1. Delete the existing multicast consumer configurations. See [Delete multicast consumer configurations](https://docs.cloud.google.com/vpc/docs/multicast/delete-resources#delete-consumers).
  2. Complete the multicast producer configuration. See [Enable a VPC network to produce multicast traffic](https://docs.cloud.google.com/vpc/docs/multicast/enable-producer-network#enable-network).
  3. Complete the multicast consumer configuration. See [Enable a VPC network to consume multicast traffic](https://docs.cloud.google.com/vpc/docs/multicast/enable-consumer-network#enable-network).



To prevent this issue from happening in the future, ensure that you complete the multicast producer configuration before the multicast consumer configuration if you plan to use the same VPC network to host both multicast producers and multicast consumers.

### Multicast consumer can't receive multicast traffic

If your multicast consumer instance can't receive multicast traffic, do the following:

  1. Ensure that firewall rules are configured to allow multicast traffic to the multicast consumer. For more information, see the following: 
     * [Multicast producer network firewall configuration](https://docs.cloud.google.com/vpc/docs/multicast/enable-producer-network#add-firewall-rules)
     * [Multicast consumer network firewall configuration](https://docs.cloud.google.com/vpc/docs/multicast/enable-consumer-network#add-firewall-rules)
  2. Confirm the following: 
     * The multicast group IP address is part of a range that has been activated by the multicast administrator
     * The multicast producer is sending traffic to the address
  3. Ensure that you have completed the steps to enable IGMP query and force IGMPv2 on the multicast consumer instance. For more information, see [Configure multicast consumer instances](https://docs.cloud.google.com/vpc/docs/multicast/configure-consumer-vms).
  4. For multicast consumer VPC networks that are part of a multicast domain that uses the Network Connectivity Center (NCC) star topology, check the state of your multicast consumer configurations as described in [View multicast consumer configurations](https://docs.cloud.google.com/vpc/docs/multicast/view-resources#view-consumer-configs).

For a multicast consumer association, a state of `INACTIVE` indicates that you have lost access to the multicast domain. For a multicast group consumer activation, a state of `INACTIVE` indicates that you have lost access to the multicast group range. For more information, contact the multicast administrator.




### Multicast producer or consumer experiencing packet loss

If a multicast producer or multicast consumer instance is experiencing packet loss, do the following:

  1. Follow the instructions to [Check network and OS statistics for packet discards due to resource exhaustion](https://docs.cloud.google.com/vpc/docs/ts-vm-vm-internal#check-stats-latency). The instance might be experiencing packet loss due to resource exhaustion, which can be caused by using a non-recommended machine type or using a machine type with insufficient vCPUs.

  2. If necessary, update the instance to use a recommended machine type or to use a machine type with more vCPUs. For more information, see [Machine considerations for multicast producers and consumers](https://docs.cloud.google.com/vpc/docs/multicast/overview#machine-requirements).




If you are still experiencing packet loss after updating your machine type, the multicast administrator might need to resize the multicast infrastructure for the domain as described in [Update multicast domain parameters](https://docs.cloud.google.com/vpc/docs/multicast/update-domain-parameters).

### Join or leave taking a long time

During Google Cloud software rollouts, the infrastructure for a multicast domain may be temporarily unavailable to process new join and leave requests. IGMP membership reports are dropped and need to be re-sent.

To avoid disruptions caused by this issue, configure redundant multicast domains as part of a domain group to help ensure that the infrastructure for one domain remains available while the other domain is being upgraded. For more information, see [Multicast domains](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#domains).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
