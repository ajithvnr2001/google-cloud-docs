---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/routes/create/
title: gcloud beta compute routes create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:11:03.798380+00:00
---

# gcloud beta compute routes create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/routes/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute routes create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute routes create - create a new route 
SYNOPSIS
    

`gcloud beta compute routes create` `NAME` `--destination-range`=`DESTINATION_RANGE` (`--next-hop-address`=`NEXT_HOP_ADDRESS` | `--next-hop-gateway`=`NEXT_HOP_GATEWAY` | `--next-hop-ilb`=`NEXT_HOP_ILB` | `--next-hop-instance`=`NEXT_HOP_INSTANCE` | `--next-hop-vpn-tunnel`=`NEXT_HOP_VPN_TUNNEL`) [`--description`=`DESCRIPTION`] [`--network`=`NETWORK`; default="default"] [`--next-hop-ilb-region`=`NEXT_HOP_ILB_REGION`] [`--next-hop-instance-zone`=`NEXT_HOP_INSTANCE_ZONE`] [`--next-hop-vpn-tunnel-region`=`NEXT_HOP_VPN_TUNNEL_REGION`] [`--priority`=`PRIORITY`; default=1000] [`--resource-manager-tags`=[`KEY`=`VALUE`,…]] [`--tags`=`TAG`,[`TAG`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute routes create` is used to create routes. A route is a rule that specifies how certain packets should be handled by the virtual network. Routes are associated with virtual machine instances by tag, and the set of routes for a particular VM is called its routing table. For each packet leaving a virtual machine, the system searches that machine's routing table for a single best matching route. 

Routes match packets by destination IP address, preferring smaller or more specific ranges over larger ones (see ``\--destination-range``). If there is a tie, the system selects the route with the smallest priority value. If there is still a tie, it uses the layer 3 and 4 packet headers to select just one of the remaining matching routes. The packet is then forwarded as specified by ``\--next-hop-address``, ``\--next-hop-instance``, ``\--next-hop-vpn-tunnel``, ``\--next-hop-gateway``, or ``\--next-hop-ilb`` of the winning route. Packets that do not match any route in the sending virtual machine routing table will be dropped. 

Exactly one of ``\--next-hop-address``, ``\--next-hop-gateway``, ``\--next-hop-vpn-tunnel``, ``\--next-hop-instance``, or ``\--next-hop-ilb`` must be provided with this command. 

EXAMPLES
     To create a route with the name 'route-name' with destination range '0.0.0.0/0' and with next hop gateway 'default-internet-gateway', run: 
    
    
    gcloud beta compute routes create route-name --destination-range=0.0.0.0/0 --next-hop-gateway=default-internet-gateway

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the route to create. 
REQUIRED FLAGS
    

`--destination-range`=`DESTINATION_RANGE`
     The destination range of outgoing packets that the route will apply to. To match all traffic, use ``0.0.0.0/0´´. 
Exactly one of these must be specified: 

`--next-hop-address`=`NEXT_HOP_ADDRESS`
     Specifies the IP address of an instance that should handle matching packets. The instance must have IP forwarding enabled (i.e., include ``\--can-ip-forward`` when creating the instance using `[gcloud compute instances create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create)`) 
`--next-hop-gateway`=`NEXT_HOP_GATEWAY`
     Specifies the gateway that should handle matching packets. Currently, the only acceptable value is `default-internet-gateway` which is a gateway operated by Google Compute Engine. 
`--next-hop-ilb`=`NEXT_HOP_ILB`
     Specifies the name or IP address of a forwarding rule for an internal TCP/UDP load balancer. The forwarding rule's `--load-balancing-scheme` must be `INTERNAL`. You can use any `--destination-range` that doesn't exactly match the destination of a subnet route and isn't more specific (has a longer subnet mask) than the destination of a subnet route. For more information, see <https://cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview#destination_range>. 
`--next-hop-instance`=`NEXT_HOP_INSTANCE`
     Specifies the name of an instance that should handle traffic matching this route. When this flag is specified, the zone of the instance must be specified using ``\--next-hop-instance-zone``. 
`--next-hop-vpn-tunnel`=`NEXT_HOP_VPN_TUNNEL`
     The target VPN tunnel that will receive forwarded traffic. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     An optional, textual description for the route. 
`--network`=`NETWORK`; default="default"
     Specifies the network to which the route will be applied. 
`--next-hop-ilb-region`=`NEXT_HOP_ILB_REGION`
     The region of the next hop forwarding rule. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--next-hop-instance-zone`=`NEXT_HOP_INSTANCE_ZONE`
     The zone of the next hop instance. If not specified, you might be prompted to select a zone (interactive mode only). `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` attempts to identify the appropriate zone by searching for resources in your currently active project. If the zone cannot be determined, `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with all available Google Cloud Platform zones. 

To avoid prompting when this flag is omitted, the user can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

`--next-hop-vpn-tunnel-region`=`NEXT_HOP_VPN_TUNNEL_REGION`
     The region of the next hop vpn tunnel. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--priority`=`PRIORITY`; default=1000
     Specifies the priority of this route relative to other routes with the same specificity. The lower the value, the higher the priority. 
`--resource-manager-tags`=[`KEY`=`VALUE`,…]
     A comma-separated list of Resource Manager tags to apply to the route. 
`--tags`=`TAG`,[`TAG`,…]
     Identifies the set of instances that this route will apply to. If no tags are provided, the route will apply to all instances in the network. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute routes create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routes/create)
    
    
    [gcloud alpha compute routes create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/routes/create)
    
    
    [gcloud preview compute routes create](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/routes/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
