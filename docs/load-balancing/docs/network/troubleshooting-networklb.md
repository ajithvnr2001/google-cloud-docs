---
url: https://docs.cloud.google.com/load-balancing/docs/network/troubleshooting-networklb/
title: Troubleshoot regional external passthrough Network Load Balancers \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:28.785691+00:00
---

# Troubleshoot regional external passthrough Network Load Balancers  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/network/troubleshooting-networklb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Troubleshoot regional external passthrough Network Load Balancers Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to troubleshoot configuration issues for a Google Cloud regional external passthrough Network Load Balancer. Before investigating issues, familiarize yourself with the following pages:

  * [Regional external passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/network)
  * [Backend service-based regional external passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service)
  * [Traffic distribution for backend service-based regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution)
  * [Target pool-based regional external passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/network/networklb-target-pools)
  * [Failover concepts for regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/networklb-failover-overview)
  * [Regional external passthrough Network Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/network/networklb-monitoring)



## Troubleshoot common issues with Network Analyzer

[Network Analyzer](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview) automatically monitors your VPC network configuration and detects both suboptimal configurations and misconfigurations. It identifies network failures, provides root cause information, and suggests possible resolutions. To learn about the different misconfiguration scenarios that are automatically detected by Network Analyzer, see [Load balancer insights](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/network-services/load-balancer) in the Network Analyzer documentation.

Network Analyzer is available in the Google Cloud console as a part of Network Intelligence Center.

[Go to Network Analyzer](https://console.cloud.google.com/net-intelligence/network-analyzer)

## Troubleshoot setup issues

### Backends have incompatible balancing modes

When creating a load balancer, you might see the error:
    
    
    Validation failed for instance group INSTANCE_GROUP:
    
    backend services 1 and 2 point to the same instance group
    but the backends have incompatible balancing_mode. Values should be the same.
    

This happens when you try to use the same backend in two different load balancers, and the backends don't have compatible balancing modes.

For more information, see the following:

  * [Restrictions and guidance for instance groups](https://docs.cloud.google.com/load-balancing/docs/backend-service#restrictions_and_guidance)
  * [Change the balancing mode of a load balancer](https://docs.cloud.google.com/load-balancing/docs/backend-service#change_balancing_mode)



## Troubleshoot general connectivity issues

If you can't connect to your regional external passthrough Network Load Balancer, check for the following common issues:

  * **Verify firewall rules.**

    * Ensure that ingress allow [firewall rules](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) are defined to permit health checks to backend VMs.
    * Ensure that ingress allow [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) allow traffic to the backend VMs from clients.
    * Ensure that relevant firewall rules exist to allow traffic to reach the backend VMs on the ports being used by the load balancer.
    * If you're using [target tags for the firewall rules](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#targets_for_firewall_rules), make sure that the load balancer's backend VMs are tagged appropriately.

To learn how to configure firewall rules required by your regional external passthrough Network Load Balancer, see [Configuring firewall rules](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service#configure-firewall-rules).

  * **Verify that the Google guest agent is running on the backend VM.** If you can connect to a healthy backend VM, but you cannot connect to the load balancer, it might be that the [Google guest agent](https://docs.cloud.google.com/compute/docs/images/guest-environment) (formerly, the Windows Guest Environment or Linux Guest Environment) on the VM is either not running or is unable to communicate with the metadata server (`metadata.google.internal`, `169.254.169.254`).

Check for the following:

    * Ensure that the Google guest agent is [installed and running on the backend VM](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#wgei).
    * Ensure that the firewall rules within the guest operating system of the backend VM (`iptables` or Windows Firewall) don't block access to the metadata server.
  * **Verify that backend VMs are accepting packets sent to the load balancer.** Each backend VM must be configured to accept packets sent to the load balancer. That is, the destination of packets delivered to the backend VMs is the IP address of the load balancer. Under most circumstances, this is implemented with a local route.

For VMs created from Google Cloud images, the [Guest agent](https://docs.cloud.google.com/compute/docs/images/guest-environment) installs the local route for the load balancer's IP address. Google Kubernetes Engine instances based on [Container-Optimized OS](https://docs.cloud.google.com/compute/docs/containers) implement this by using `iptables` instead.

On a Linux backend VM, you can verify the presence of the local route by running the following command. Replace `LOAD_BALANCER_IP` with the load balancer's IP address:
        
        sudo ip route list table local | grep LOAD_BALANCER_IP
        

  * **Verify service IP address and port binding on the backend VMs.** Packets sent to a regional external passthrough Network Load Balancer arrive at backend VMs with the destination IP address of the load balancer itself. This type of load balancer is not a proxy, and this is expected behavior.

To see the services listening on a port, run the following command:
        
        netstat -nl | grep ':PORT'
        

The software running on the backend VM must be doing the following:

    * Listening on (bound to) the load balancer's IP address or any IP address (`0.0.0.0` or `::`)
    * Listening on (bound to) a port that's included in the load balancer's forwarding rule

To test this, connect to a backend VM by using either SSH or RDP. Then perform the following tests by using either `curl`, `telnet`, or a similar tool:

    * Attempt to reach the service by contacting it using the internal IP address of the backend VM itself, `127.0.0.1`, or localhost.
    * Attempt to reach the service by contacting it using the IP address of the load balancer's forwarding rule.
  * **Verify that health check traffic can reach backend VMs.** To verify that health check traffic reaches your backend VMs, [enable health check logging](https://docs.cloud.google.com/load-balancing/docs/health-check-logging) and search for successful log entries.




## Troubleshoot Shared VPC issues

If you are using Shared VPC and you cannot create a new regional external passthrough Network Load Balancer in a particular subnet, an organization policy might be the cause. In the organization policy, add the subnet to the list of allowed subnets or contact your organization administrator. For more information, see the [`constraints/compute.restrictSharedVpcSubnetworks`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) constraint.

## Troubleshoot failover issues

If you've configured failover for a regional external passthrough Network Load Balancer, use the following steps to verify your configuration:

  * Make sure that you understand [Backend selection and connection tracking](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#connection-tracking) and [Failover](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#failover) concepts.
  * Make sure that you've designated at least one failover backend.
  * Review which backends are healthy using the Google Cloud console or `gcloud compute backend-services get-health` so that you can determine which VMs are eligible backends.
  * Make sure that the failover ratio is set appropriately.
  * We don't recommend using managed instance groups that have autoscaling enabled in conjunction with failover because autoscaling changes the number of primary backends, failover backends, or both. This can result in the set of eligible backends changing unexpectedly because the failover ratio is fixed.
  * If a client VM is also a load-balanced backend VM, connections to the load balancer's forwarding rule IP address are sent to the backend VM itself. For more information, see [Testing from a single client](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#single_client_tests).



## Troubleshoot logging issues

If you configure logging for a regional external passthrough Network Load Balancer, the following issues might occur:

  * RTT measurements such as byte values might be missing in some of the logs if not enough packets are sampled to capture RTT. This is more likely to happen for low volume connections.
  * RTT values are available only for TCP flows.
  * Some packets are sent with no payload. If header-only packets are sampled, the bytes value is `0`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
