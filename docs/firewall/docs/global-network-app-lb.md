---
url: https://docs.cloud.google.com/firewall/docs/global-network-app-lb/
title: Use global network firewall policies to protect Envoy-based load balancers \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:25.062143+00:00
---

# Use global network firewall policies to protect Envoy-based load balancers  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/global-network-app-lb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Use global network firewall policies to protect Envoy-based load balancers Stay organized with collections  Save and categorize content based on your preferences. 

To restrict traffic to the managed Envoy proxies in a [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets), you can configure global network firewall policies to protect internal Application Load Balancers and internal proxy Network Load Balancers.

This document describes how to set up a global network firewall policy rule that applies to internal Application Load Balancers and internal proxy Network Load Balancers.

Internal Application Load Balancers and internal proxy Network Load Balancers have the following firewall rule requirements and options:

  * **Firewall rules that apply to the load balancer backends** : If you use instance groups or `GCE_VM_IP_PORT` zonal Network Endpoint Groups (NEG) backends, you must configure firewall rules that allow the managed Envoy proxies to connect to the backend VMs.

  * **Firewall rules that apply to the managed Envoy proxies** : These rules provide optional access control for load balancer forwarding rules. This is useful if the load balancer uses [regional internet NEGs](https://docs.cloud.google.com/load-balancing/docs/negs#internet-neg) or [ Private Service Connect NEGs](https://docs.cloud.google.com/load-balancing/docs/negs#psc-neg).




### Create the load balancing resources

Before you configure firewall rules and policies, set up the required load balancing resources. These resources include a Virtual Private Cloud (VPC) network, subnets, a load balancer with backends and a forwarding rule, and a client VM instance for testing connectivity.

To create and configure the resources for your chosen load balancer, see the following documents:

  * [Set up a cross-region internal Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-internal)
  * [Set up a regional internal Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal)
  * [Set up a cross-region internal proxy Network Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/tcp/setup-cross-reg-proxy-migs)
  * [Set up a regional internal proxy Network Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs)



After you create the resources, note the following details. Use these details to configure firewall rules and policies later on this page:

  * The name and IP address of the forwarding rule
  * The name of the VPC network
  * The source IP address that connects to the load balancer. For testing, this address can be the IP address of the test VM instance that you created to verify connectivity with the load balancer.



### Create Cloud NGFW resources

  1. Create a global network firewall policy. For more information, see [Create a global network firewall policy](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#create-network-firewall-policy).

  2. Associate the firewall policy with the VPC network.

To apply firewall policy rules to a load balancer forwarding rule, you must [associate the policy with the VPC network](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#associate) that contains the forwarding rule. Associating the policy activates the rules on that network.

  3. To control traffic that reaches the load balancer, [create ingress firewall rules in a global network firewall policy](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#create-ingress-rule-target-lb). Unlike VM targets, ingress is allowed when no firewall rules apply to the managed Envoy proxies used by internal Application Load Balancers and internal proxy Network Load Balancers. To restrict access to one or more load balancer forwarding rules, you must create ingress firewall firewall rules with the `--target-type=INTERNAL_MANAGED_LB` parameter:

     * One lower-priority ingress `deny` firewall rule with `--src-ip-ranges=0.0.0.0/0`. This sets a baseline that denies all incoming traffic.

     * One or more higher-priority ingress `allow` firewall rules with `--src-ip-ranges` that include the following ranges:

       * The IP addresses of the approved clients.

       * The IP addresses of the Google health check probes. For more information, see [Probe IP ranges for select managed Envoy-based load balancer frontends](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges-mes-frontends) in the Health checks overview.

To target a specific forwarding rule, set `--target-forwarding-rules` to a single load balancer forwarding rule in the [supported format](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#lb-forwarding-rules). If you want to apply the firewall policy and its rules to internal Application Load Balancers and internal proxy Network Load Balancers of a VPC network, don't specify the `--target-forwarding-rules` flag.

  4. View firewall logs. For more information, see [View logs](https://docs.cloud.google.com/firewall/docs/manage-firewall-policy-rules-logging#viewing_logs).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
