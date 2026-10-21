---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/add-interface/
title: gcloud compute routers add-interface \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:01:03.096071+00:00
---

# gcloud compute routers add-interface  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/add-interface/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute routers add-interface Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute routers add-interface - add an interface to a Compute Engine router 
SYNOPSIS
    

`gcloud compute routers add-interface` `NAME` `--interface-name`=`INTERFACE_NAME` (`--interconnect-attachment`=`INTERCONNECT_ATTACHMENT` `--interconnect-attachment-region`=`INTERCONNECT_ATTACHMENT_REGION` | `--subnetwork`=`SUBNETWORK` `--subnetwork-region`=`SUBNETWORK_REGION` | `--vpn-tunnel`=`VPN_TUNNEL` `--vpn-tunnel-region`=`VPN_TUNNEL_REGION`) [`--ip-address`=`IP_ADDRESS`] [`--ip-version`=`IP_VERSION`] [`--mask-length`=`MASK_LENGTH`] [`--redundant-interface`=`REDUNDANT_INTERFACE`] [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute routers add-interface` is used to add an interface to a Compute Engine router. 
POSITIONAL ARGUMENTS
    

`NAME`
     Name of the router to update. 
REQUIRED FLAGS
    

`--interface-name`=`INTERFACE_NAME`
     The name of the interface being added. 
Exactly one of these must be specified: 

Interconnect Attachment 
`--interconnect-attachment`=`INTERCONNECT_ATTACHMENT`
     The interconnect attachment of the interface being added. 
`--interconnect-attachment-region`=`INTERCONNECT_ATTACHMENT_REGION`
     Region of the interconnectAttachment to operate on. If not specified it will be set to the region of the router. Overrides the default `compute/region` property value for this command invocation. 
Subnetwork 
`--subnetwork`=`SUBNETWORK`
     The subnetwork of the interface being added. 
`--subnetwork-region`=`SUBNETWORK_REGION`
     Region of the subnetwork to operate on. If not specified it will be set to the region of the router. Overrides the default `compute/region` property value for this command invocation. 
VPN Tunnel 
`--vpn-tunnel`=`VPN_TUNNEL`
     The tunnel of the interface being added. 
`--vpn-tunnel-region`=`VPN_TUNNEL_REGION`
     Region of the vpn tunnel to operate on. If not specified it will be set to the region of the router. Overrides the default `compute/region` property value for this command invocation. 
OPTIONAL FLAGS
    

`--ip-address`=`IP_ADDRESS`
     The link local (IPv4) or ULA (IPv6) address of the router for this interface. 
`--ip-version`=`IP_VERSION`
     IP version of the interface. Possible values are IPV4 and IPV6. Defaults to IPV4. `IP_VERSION` must be one of: 

`IPV4`
     Interface with IPv4-based BGP. 
`IPV6`
     Interface with IPv6-based BGP. 
`--mask-length`=`MASK_LENGTH`
     The subnet mask for the IP range of the interface. The interface IP address and BGP peer IP address must be selected from the subnet defined by this range. 
`--redundant-interface`=`REDUNDANT_INTERFACE`
     The interface that is redundant to the current interface. 
`--region`=`REGION`
     Region of the router to update. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute routers add-interface](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/routers/add-interface)
    
    
    [gcloud beta compute routers add-interface](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/routers/add-interface)
    
    
    [gcloud preview compute routers add-interface](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/routers/add-interface)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
