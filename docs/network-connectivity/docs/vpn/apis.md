---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/apis/
title: APIs and reference \u00a0|\u00a0 Cloud VPN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:42:47.776562+00:00
---

# APIs and reference  |  Cloud VPN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Reference ](https://docs.cloud.google.com/network-connectivity/docs/vpn/apis)



Send feedback 

#  APIs and reference Stay organized with collections  Save and categorize content based on your preferences. 

## API resource types

The Cloud VPN API and `gcloud` commands are part of Compute Engine. The following sections cover API resources for HA VPN and Classic VPN.

### HA VPN resources

  * [`vpnGateways`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnGateways): a HA VPN gateway resource
  * [`vpnTunnels`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels): a VPN tunnel resource
  * [`externalVpnGateways`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/externalVpnGateways): in Google Cloud, your [peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/key-terms#peer-definition) device or service



### Classic VPN resources

  * [`forwardingRules`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules): three forwarding rules that direct UDP and ESP traffic to the target VPN gateway
  * [`targetVpnGateways`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways): a Classic VPN gateway resource
  * [`vpnTunnels`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels): a VPN tunnel resource



## `gcloud` commands

For more information about the `gcloud` commands for these resources, see the following Google Cloud CLI documentation.

### HA VPN commands

  * [`gcloud compute vpn-gateways`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways)
  * [`gcloud compute external-vpn-gateways`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/external-vpn-gateways)
  * [`gcloud compute vpn-tunnels`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels)



### Classic VPN commands

  * [`gcloud compute forwarding-rules`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules)
  * [`gcloud compute target-vpn-gateways`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-vpn-gateways)
  * [`gcloud compute vpn-tunnels`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels)



## Related APIs and `gcloud` commands

The following Compute Engine API reference and `gcloud` commands support common Compute Engine networking functions and can be useful when configuring Cloud VPN:

  * Google Cloud projects  
[API](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects) | [`gcloud` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects)
  * Virtual machine (VM) instances  
[API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances) | [`gcloud` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances)
  * Virtual Private Cloud (VPC) networks and subnets  
[API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks) | [`gcloud` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks)
  * Firewall rules  
[API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls) | [`gcloud` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules)
  * Forwarding rules  
[API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules) | [`gcloud` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules)
  * Routes  
[API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routes) | [`gcloud` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routes)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
