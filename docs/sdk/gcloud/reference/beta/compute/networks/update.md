---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/networks/update/
title: gcloud beta compute networks update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:02:52.311460+00:00
---

# gcloud beta compute networks update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/networks/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute networks update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute networks update - update a Compute Engine network 
SYNOPSIS
    

`gcloud beta compute networks update` `NAME` [`--async`] [`--[no-]enable-ula-internal-ipv6`] [`--internal-ipv6-range`=`INTERNAL_IPV6_RANGE`] [`--mtu`=`MTU`] [`--network-firewall-policy-enforcement-order`=`NETWORK_FIREWALL_POLICY_ENFORCEMENT_ORDER`] [`--bgp-best-path-selection-mode`=`BGP_BEST_PATH_SELECTION_MODE` `--[no-]bgp-bps-always-compare-med` `--bgp-bps-inter-region-cost`=`BGP_BPS_INTER_REGION_COST`] [`--bgp-routing-mode`=`MODE` | `--switch-to-custom-subnet-mode`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute networks update` is used to update Compute Engine networks. 
EXAMPLES
     To update regional network with the name 'network-name' to global, run: 
    
    
    gcloud beta compute networks update network-name --bgp-routing-mode=global

To update an auto subnet mode network with the name 'network-name' to custom subnet mode, run: 
    
    
    gcloud beta compute networks update network-name --switch-to-custom-subnet-mode

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the network to operate on. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--[no-]enable-ula-internal-ipv6`
     Enable/disable ULA internal IPv6 on this network. Enabling this feature will assign a /48 from google defined ULA prefix fd20::/20. 

Use `--enable-ula-internal-ipv6` to enable and `--no-enable-ula-internal-ipv6` to disable. 

`--internal-ipv6-range`=`INTERNAL_IPV6_RANGE`
     When enabling ULA internal IPv6, caller can optionally specify the /48 range they want from the google defined ULA prefix fd20::/20. ULA_IPV6_RANGE must be a valid /48 ULA IPv6 address and within the fd20::/20. Operation will fail if the speficied /48 is already in used by another resource. If the field is not speficied, then a /48 range will be randomly allocated from fd20::/20 and returned via this field. 
`--mtu`=`MTU`
     Maximum transmission unit (MTU) is the size of the largest IP packet that can be transmitted on this network. Default value is 1460 bytes. The minimum value is 1300 bytes and the maximum value is 8896 bytes. The MTU advertised via DHCP to all instances attached to this network. 
`--network-firewall-policy-enforcement-order`=`NETWORK_FIREWALL_POLICY_ENFORCEMENT_ORDER`
     The Network Firewall Policy enforcement order of this network. If not specified, defaults to AFTER_CLASSIC_FIREWALL. 

`NETWORK_FIREWALL_POLICY_ENFORCEMENT_ORDER` must be one of: 

`AFTER_CLASSIC_FIREWALL`
     Network Firewall Policy is enforced after classic firewall. 
`BEFORE_CLASSIC_FIREWALL`
     Network Firewall Policy is enforced before classic firewall. 
BGP Best Path Selection flags 
`--bgp-best-path-selection-mode`=`BGP_BEST_PATH_SELECTION_MODE`
     The BGP best path selection algorithm to be employed. `BGP_BEST_PATH_SELECTION_MODE` must be one of: 

`LEGACY`
     Dynamic routes are ranked based on the multiple exit-discriminator (MED) BGP attribute. When global routing is enabled, the MED of the routes received from other regions is the original MED plus the region-to-region cost. 
`STANDARD`
     Dynamic routes are ranked based on AS Path, Origin, Neighbor ASN and MED BGP attributes. When global routing is enabled, region-to-region cost is used as a tiebreaker. This mode offers customizations to fine-tune BGP best path routing with additional flags like --bgp-bps-always-compare-med and \--bgp-bps-inter-region-cost 
`--[no-]bgp-bps-always-compare-med`
     Enables/disables the comparison of MED across routes with different Neighbor ASNs. This value can only be set if the --bgp-best-path-selection-mode is STANDARD. Use `--bgp-bps-always-compare-med` to enable and `--no-bgp-bps-always-compare-med` to disable. 
`--bgp-bps-inter-region-cost`=`BGP_BPS_INTER_REGION_COST`
     Defines the preferred approach for handling inter-region cost in the selection process. This value can only be set if the --bgp-best-path-selection-mode is STANDARD. `BGP_BPS_INTER_REGION_COST` must be one of: 

`ADD_COST_TO_MED`
     Adds inter-region cost to the MED before comparing the MED value. When multiple routes have the same value after the Add-cost-to-med comparison, the route selection continues and prefers the route with lowest cost. 
`DEFAULT`
     MED is compared as originally received from peers. When multiple routes have the same MED, cost is evaluated as the next step. 
At most one of these can be specified: 

`--bgp-routing-mode`=`MODE`
     The target BGP routing mode for this network. `MODE` must be one of: 

`global`
     Cloud Routers in this network advertise subnetworks from all regions to their BGP peers, and program instances in all regions with the router's best learned BGP routes. 
`regional`
     Cloud Routers in this network advertise subnetworks from their local region only to their BGP peers, and program instances in their local region only with the router's best learned BGP routes. 
`--switch-to-custom-subnet-mode`
     Switch to custom subnet mode. This action cannot be undone. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute networks update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/update)
    
    
    [gcloud alpha compute networks update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/networks/update)
    
    
    [gcloud preview compute networks update](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/networks/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
