---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/create/
title: gcloud compute packet-mirrorings create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:16:12.885192+00:00
---

# gcloud compute packet-mirrorings create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute packet-mirrorings create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute packet-mirrorings create - create a Compute Engine packet mirroring policy 
SYNOPSIS
    

`gcloud compute packet-mirrorings create` `NAME` `--collector-ilb`=`COLLECTOR_ILB` `--network`=`NETWORK` [`--async`] [`--description`=`DESCRIPTION`] [`--no-enable`] [`--filter-cidr-ranges`=[`CIDR_RANGE`,…]] [`--filter-direction`=`DIRECTION`] [`--filter-protocols`=[`PROTOCOL`,…]] [`--mirrored-instances`=[`INSTANCE`,…]] [`--mirrored-subnets`=[`SUBNET`,…]] [`--mirrored-tags`=[`TAG`,…]] [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a Compute Engine packet mirroring policy. 
EXAMPLES
     Mirror all tcp traffic to/from all instances in subnet my-subnet in us-central1, and send the mirrored traffic to the collector-fr Forwarding Rule. 
    
    
    gcloud compute packet-mirrorings create my-pm --network my-network --region us-central1 --mirrored-subnets my-subnet --collector-ilb collector-fr --filter-protocols tcp

Mirror all traffic between instances with tag t1 and external server with IP 11.22.33.44 in us-central1, and send the mirrored traffic to the collector-fr Forwarding Rule. 
    
    
    gcloud compute packet-mirrorings create my-pm --network my-network --region us-central1 --mirrored-tags t1 --collector-ilb collector-fr --filter-cidr-ranges 11.22.33.44/32

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the packet mirroring to create. 
REQUIRED FLAGS
    

`--collector-ilb`=`COLLECTOR_ILB`
     Forwarding rule configured as collector. This must be a regional forwarding rule (in the same region) with load balancing scheme INTERNAL and isMirroringCollector set to true. 

You can provide this as the full URL to the forwarding rule, partial URL, or name. For example, the following are valid values: 

  * <https://compute.googleapis.com/compute/v1/projects/myproject/> regions/us-central1/forwardingRules/fr-1 
  * projects/myproject/regions/us-central1/forwardingRules/fr-1 
  * fr-1 


`--network`=`NETWORK`
     Network for this packet mirroring. Only the packets in this network will be mirrored. It is mandatory that all mirrored VMs have a network interface controller (NIC) in the given network. All mirrored subnetworks should belong to the given network. 

You can provide this as the full URL to the network, partial URL, or name. For example, the following are valid values: 

  * <https://compute.googleapis.com/compute/v1/projects/myproject/> global/networks/network-1 
  * projects/myproject/global/networks/network-1 
  * network-1 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     Optional, textual description for the packet mirroring. 
`--enable`
     Enable or disable the packet-mirroring. Enabled by default, use `--no-enable` to disable. 
`--filter-cidr-ranges`=[`CIDR_RANGE`,…]
     One or more IPv4 or IPv6 CIDR ranges that apply as filters on the source (ingress) or destination (egress) IP in the IP header. If no ranges are specified, all IPv4 traffic that matches the specified IPProtocols is mirrored. If neither cidrRanges nor IPProtocols is specified, all IPv4 traffic is mirrored. To mirror all IPv4 and IPv6 traffic, use 0.0.0.0/0,::/0 
`--filter-direction`=`DIRECTION`
    

  * For `ingress`, only ingress traffic is mirrored. 
  * For `egress`, only egress traffic is mirrored. 
  * For `both` (default), both directions are mirrored. `DIRECTION` must be one of: `both`, `egress`, `ingress`. 


`--filter-protocols`=[`PROTOCOL`,…]
     List of IP protocols that apply as filters for packet mirroring traffic. If unspecified, the packet mirroring applies to all traffic. PROTOCOL can be one of tcp, udp, icmp, esp, ah, ipip, sctp, or an IANA protocol number. 
`--mirrored-instances`=[`INSTANCE`,…]
     List of instances to be mirrored. You can provide this as the full or valid partial URL to the instance. For example, the following are valid values: 

  * <https://compute.googleapis.com/compute/v1/projects/myproject/> zones/us-central1-a/instances/instance- 
  * projects/myproject/zones/us-central1-a/instances/instance-1 


`--mirrored-subnets`=[`SUBNET`,…]
     List of subnets to be mirrored. You can provide this as the full URL to the subnet, partial URL, or name. For example, the following are valid values: 

  * <https://compute.googleapis.com/compute/v1/projects/myproject/> regions/us-central1/subnetworks/subnet-1 
  * projects/myproject/regions/us-central1/subnetworks/subnet-1 
  * subnet-1 


`--mirrored-tags`=[`TAG`,…]
     List of virtual machine instance tags to be mirrored. 

To read more about configuring network tags, read this guide: <https://cloud.google.com/vpc/docs/add-remove-network-tags>

The virtual machines with the provided tags must live in zones contained in the same region as this packet mirroring. 

`--region`=`REGION`
     Region of the packet mirroring to create. Overrides the default `compute/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute packet-mirrorings create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/packet-mirrorings/create)
    
    
    [gcloud beta compute packet-mirrorings create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/packet-mirrorings/create)
    
    
    [gcloud preview compute packet-mirrorings create](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/packet-mirrorings/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
