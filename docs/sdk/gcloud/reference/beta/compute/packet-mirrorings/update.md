---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/packet-mirrorings/update/
title: gcloud beta compute packet-mirrorings update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:12:02.981498+00:00
---

# gcloud beta compute packet-mirrorings update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/packet-mirrorings/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute packet-mirrorings update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute packet-mirrorings update - update a Compute Engine packet mirroring policy 
SYNOPSIS
    

`gcloud beta compute packet-mirrorings update` `NAME` [`--async`] [`--collector-ilb`=`COLLECTOR_ILB`] [`--description`=`DESCRIPTION`] [`--enable`] [`--filter-direction`=`DIRECTION`] [`--region`=`REGION`] [`--add-filter-cidr-ranges`=[`CIDR_RANGE`,…] | `--clear-filter-cidr-ranges` | `--remove-filter-cidr-ranges`=[`CIDR_RANGE`,…] | `--set-filter-cidr-ranges`=[`CIDR_RANGE`,…]] [`--add-filter-protocols`=[`PROTOCOL`,…] | `--clear-filter-protocols` | `--remove-filter-protocols`=[`PROTOCOL`,…] | `--set-filter-protocols`=[`PROTOCOL`,…]] [`--add-mirrored-instances`=[`INSTANCE`,…] | `--clear-mirrored-instances` | `--remove-mirrored-instances`=[`INSTANCE`,…] | `--set-mirrored-instances`=[`INSTANCE`,…]] [`--add-mirrored-subnets`=[`SUBNET`,…] | `--clear-mirrored-subnets` | `--remove-mirrored-subnets`=[`SUBNET`,…] | `--set-mirrored-subnets`=[`SUBNET`,…]] [`--add-mirrored-tags`=[`TAG`,…] | `--clear-mirrored-tags` | `--remove-mirrored-tags`=[`TAG`,…] | `--set-mirrored-tags`=[`TAG`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update a Compute Engine packet mirroring policy. 
EXAMPLES
     Stop mirroring by tags, add subnet-1 as a mirrored subnet. 
    
    
    gcloud beta compute packet-mirrorings update my-pm --region us-central1 --clear-mirrored-tags --add-mirrored-subnets subnet-1

Change the load-balancer to send mirrored traffic to. 
    
    
    gcloud beta compute packet-mirrorings update my-pm --region us-central1 --collector-ilb new-forwarding-rule

Disable a Packet Mirroring policy. 
    
    
    gcloud beta compute packet-mirrorings update my-pm --region us-central1 --no-enable

Re-enable a disabled Packet Mirroring policy. 
    
    
    gcloud beta compute packet-mirrorings update my-pm --region us-central1 --enable

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the packet mirroring to update. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--collector-ilb`=`COLLECTOR_ILB`
     Forwarding rule configured as collector. This must be a regional forwarding rule (in the same region) with load balancing scheme INTERNAL and isMirroringCollector set to true. 

You can provide this as the full URL to the forwarding rule, partial URL, or name. For example, the following are valid values: 

  * <https://compute.googleapis.com/compute/v1/projects/myproject/> regions/us-central1/forwardingRules/fr-1 
  * projects/myproject/regions/us-central1/forwardingRules/fr-1 
  * fr-1 


`--description`=`DESCRIPTION`
     Optional, textual description for the packet mirroring. 
`--enable`
     Enable or disable the packet-mirroring. 
`--filter-direction`=`DIRECTION`
    

  * For `ingress`, only ingress traffic is mirrored. 
  * For `egress`, only egress traffic is mirrored. 
  * For `both` (default), both directions are mirrored. `DIRECTION` must be one of: `both`, `egress`, `ingress`. 


`--region`=`REGION`
     Region of the packet mirroring to update. Overrides the default `compute/region` property value for this command invocation. 
Update the filter CIDR ranges of this packet mirroring. 

At most one of these can be specified: 

`--add-filter-cidr-ranges`=[`CIDR_RANGE`,…]
     List of filter CIDR ranges to add to the packet mirroring. 
`--clear-filter-cidr-ranges`
     If specified, clear the existing filter CIDR ranges from the packet mirroring. 
`--remove-filter-cidr-ranges`=[`CIDR_RANGE`,…]
     List of filter CIDR ranges to remove from the packet mirroring. 
`--set-filter-cidr-ranges`=[`CIDR_RANGE`,…]
     List of filter CIDR ranges to be mirrored on the packet mirroring. 
Update the filter protocols of this packet mirroring. 

At most one of these can be specified: 

`--add-filter-protocols`=[`PROTOCOL`,…]
     List of filter IP protocols to add to the packet mirroring. PROTOCOL can be one of tcp, udp, icmp, esp, ah, ipip, sctp, or an IANA protocol number. 
`--clear-filter-protocols`
     If specified, clear the existing filter IP protocols from the packet mirroring. 
`--remove-filter-protocols`=[`PROTOCOL`,…]
     List of filter IP protocols to remove from the packet mirroring. PROTOCOL can be one of tcp, udp, icmp, esp, ah, ipip, sctp, or an IANA protocol number. 
`--set-filter-protocols`=[`PROTOCOL`,…]
     List of filter IP protocols to be mirrored on the packet mirroring. PROTOCOL can be one of tcp, udp, icmp, esp, ah, ipip, sctp, or an IANA protocol number. 
Update the mirrored instances of this packet mirroring. At most one of these can be specified: 

`--add-mirrored-instances`=[`INSTANCE`,…]
     List of instances to add to the packet mirroring. 
`--clear-mirrored-instances`
     If specified, clear the existing instances from the packet mirroring. 
`--remove-mirrored-instances`=[`INSTANCE`,…]
     List of instances to remove from the packet mirroring. 
`--set-mirrored-instances`=[`INSTANCE`,…]
     List of instances to be mirrored on the packet mirroring. 
Update the mirrored subnets of this packet mirroring. At most one of these can be specified: 

`--add-mirrored-subnets`=[`SUBNET`,…]
     List of subnets to add to the packet mirroring. 
`--clear-mirrored-subnets`
     If specified, clear the existing subnets from the packet mirroring. 
`--remove-mirrored-subnets`=[`SUBNET`,…]
     List of subnets to remove from the packet mirroring. 
`--set-mirrored-subnets`=[`SUBNET`,…]
     List of subnets to be mirrored on the packet mirroring. 
Update the mirrored tags of this packet mirroring. 
    
    
    To read more about configuring network tags, read this guide:
    <https://cloud.google.com/vpc/docs/add-remove-network-tags>
    
    
    The virtual machines with the provided tags must live
    in zones contained in the same region as this packet mirroring.

At most one of these can be specified: 

`--add-mirrored-tags`=[`TAG`,…]
     List of tags to add to the packet mirroring. 
`--clear-mirrored-tags`
     If specified, clear the existing tags from the packet mirroring. 
`--remove-mirrored-tags`=[`TAG`,…]
     List of tags to remove from the packet mirroring. 
`--set-mirrored-tags`=[`TAG`,…]
     List of tags to be mirrored on the packet mirroring. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute packet-mirrorings update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update)
    
    
    [gcloud alpha compute packet-mirrorings update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/packet-mirrorings/update)
    
    
    [gcloud preview compute packet-mirrorings update](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/packet-mirrorings/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
