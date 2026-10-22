---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-networking/
title: Troubleshooting common networking issues \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:16.525182+00:00
---

# Troubleshooting common networking issues  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting common networking issues Stay organized with collections  Save and categorize content based on your preferences. 

## Troubleshoot network latency issues

For information about the ways you can improve connection latency between processes within Google Cloud and decrease the latency of TCP connections, see [TCP optimization for network performance in Google Cloud and hybrid scenarios](https://docs.cloud.google.com/compute/docs/networking/tcp-optimization-for-network-performance-in-gcp-and-hybrid).

## Troubleshooting dropped network traffic

Compute Engine only allows network traffic that is explicitly permitted by your project's [Firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) to reach your instance. By default, all projects automatically come with a [default network](https://docs.cloud.google.com/compute/docs/networks-and-firewalls#networks) that allows [certain kinds of connections](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules). If you deny all traffic, by default, that also denies SSH connections and all internal traffic. For more information, see the [Firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) page.

In addition, you may need to adjust TCP keep-alive settings to work around the default idle connection timeout of 10 minutes. For more information, see [Communicating between your instances and the internet](https://docs.cloud.google.com/compute/docs/troubleshooting#communicatewithinternet).

## Troubleshooting firewall rules or routes on an instance

The Google Cloud console provides network details for each network interface of an instance. You can view all of the firewall rules or routes that apply to an interface, or you can view just the rules and routes that the interface uses. Either view can help you troubleshoot which firewall rules and routes apply to the instance and which ones are actually being used (where priority and processing order override other rules or routes).

For more information, see the troubleshooting information in the Virtual Private Cloud documentation:

  * [Listing firewalls rules for a network interface](https://docs.cloud.google.com/vpc/docs/using-firewalls#listing-rules-vm)
  * [Listing routes for a network interface](https://docs.cloud.google.com/vpc/docs/using-routes#listing-routes-vm)



## Troubleshooting protocol forwarding for private forwarding rules

Use the following sections to resolve common issue related to protocol forwarding for private forwarding rules.

### Regional restriction

Protocol forwarding for private forwarding rules is a regional product. All clients and target instance VMs must be in the same region.

### Error message: "An internal target instance can only be the target of one forwarding rule"

If you see the error message `An internal target instance can only be the target of one forwarding rule`, you might be trying to configure two forwarding rules pointing to the same target instance. You cannot point multiple forwarding rules to the same target instance.

## Troubleshooting latency on Compute Engine instances when processing high packet rates

If your VM experiences latency, dropped packets, or packet retransmissions when processing high packet rates, your VM might not have enough receive queues (RX) or transmit queues (TX) on the network interface (NIC) processing those packets.

To resolve these issues, see [Receive and transmit queues](https://docs.cloud.google.com/compute/docs/network-bandwidth#rx-tx) for information about how Compute Engine allocates RX and TX queues.

## Troubleshooting custom NIC queue oversubscription

With queue oversubscription, the maximum queue count for the VM is:
    
    
    [maximum queue count per VM] * [number of NICs]
    

However, you must satisfy the conditions specified in [Custom queue allocation](https://docs.cloud.google.com/compute/docs/network-bandwidth). For example, if you didn't specify a custom queue count for one of the NICs configured for the VM, you get an error similar to the following:
    
    
    ERROR: (gcloud.compute.instances.create) Could not fetch resource:
     - Invalid value for field 'resource.networkInterfaces': ''. The total
     networking queue number is more than the number of vCPUs. Please specify
     the queue count for all of the interfaces.
    

## Projects migrated to zonal DNS but VMs in new project are using global DNS

If you completed the migration of your existing projects from using global DNS to using zonal DNS, but discover that VMs in a newly created project have global DNS names, you didn't enforce the boolean organization policy `constraints/compute.setNewProjectDefaultToZonalDNSOnly` at an organization or folder level. This policy overrides the default DNS setting, so that newly created projects use internal zonal DNS by default.

For instructions on enforcing this policy, see [Enforce zonal DNS only by default for new projects](https://docs.cloud.google.com/compute/docs/networking/zonal-dns#enforce_dns_by_policy).

If you aren't using an organization policy, but instead use the metadata entry `VmDnsSetting=ZonalOnly` for projects or VMs, check the metadata value for the VM. If the VM has `VmDnsSetting=GlobalDefault` configured in its metadata, this value overrides the metadata value set at the project level.

For information about how to set project metadata or VM metadata values, see [Setting custom metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata).

## Hide the zonal DNS migration banner in the Google Cloud console

The zonal DNS migration notification banner provides assistance in migrating your projects to zonal DNS. If you dismiss the banner, but want it to appear again, you must contact Cloud Customer Care for assistance.

To hide the zonal DNS migration notification banner, click the **Dismiss** button in the banner that appears on the **VM instances** page of the Google Cloud console. If you click the button, the banner no longer appears for the project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
