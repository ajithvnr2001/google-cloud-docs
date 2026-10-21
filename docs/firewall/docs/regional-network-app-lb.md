---
url: https://docs.cloud.google.com/firewall/docs/regional-network-app-lb/
title: Use regional network firewall policies to protect internal Application Load Balancers and internal proxy Network Load Balancers \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:25.517347+00:00
---

# Use regional network firewall policies to protect internal Application Load Balancers and internal proxy Network Load Balancers  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/regional-network-app-lb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Use regional network firewall policies to protect internal Application Load Balancers and internal proxy Network Load Balancers Stay organized with collections  Save and categorize content based on your preferences. 

You can configure rules in Cloud Next Generation Firewall (Cloud NGFW) firewall policies that apply to managed Envoy proxies used by internal Application Load Balancer and internal proxy Network Load Balancer. These proxies run in a [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets).

Internal Application Load Balancers and internal proxy Network Load Balancers have the following firewall rule requirements and options:

  * **Firewall rules that apply to the load balancer backends** : If you use instance group or `GCE_VM_IP_PORT` zonal Network Endpoint Group (NEG) backends, you must configure firewall rules that allow the managed Envoy proxies to connect to the backend VMs.

  * **Firewall rules that apply to the managed Envoy proxies** : These firewall rules apply to the managed Envoy proxies. The rules provide optional access control to load balancer forwarding rules, which is useful when the load balancer uses [regional internet NEGs](https://docs.cloud.google.com/load-balancing/docs/negs#internet-neg) or [ Private Service Connect NEGs](https://docs.cloud.google.com/load-balancing/docs/negs#psc-neg).




This document describes how to set up the firewall rules that apply to the managed Envoy proxies.

### Create the load balancing resources

Before you configure firewall rules and policies, set up the load balancing resources, such as a Virtual Private Cloud (VPC) network, subnets, a load balancer with its backends and a forwarding rule, and a client VM instance for testing connectivity.

To create and configure the resources for your chosen load balancer, see the following documents:

  * [Set up a cross-region internal Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-internal)
  * [Set up a regional internal Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal)
  * [Set up a cross-region internal proxy Network Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/tcp/setup-cross-reg-proxy-migs)
  * [Set up a regional internal proxy Network Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs)



After creating the resources, record the following details. You will use these details to configure firewall rules and policies later in this document:

  * The region of the load balancer
  * The name and IP address of the forwarding rule
  * The name of the VPC network
  * The name, zone, and IP address of the client VM instance that you created to test load balancer connectivity



### Create Cloud NGFW resources

  1. Create a regional network firewall policy in the same region as the load balancer. For more information, see [Create a regional network firewall policy](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies#create-network-firewall-policy).

  2. Associate the firewall policy with the VPC network.

For a firewall policy's rules to apply to a load balancer forwarding rule, you must [associate the policy with the VPC network](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#associate) where that forwarding rule exists. This association activates the firewall policy's rules on the VPC network.

  3. To control the traffic that reaches the load balancer, [create ingress firewall rules in a regional network firewall policy](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies#create-ingress-rule-target-lb). Unlike VM targets, ingress is allowed when no firewall rules apply to the managed Envoy proxies used by internal Application Load Balancers and internal proxy Network Load Balancers. To restrict access to one or more load balancer forwarding rules, you must create ingress firewall firewall rules with the `--target-type=INTERNAL_MANAGED_LB` parameter:

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
