---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/vpn-gateways/create/
title: gcloud beta compute vpn-gateways create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:30:26.683296+00:00
---

# gcloud beta compute vpn-gateways create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/vpn-gateways/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute vpn-gateways create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute vpn-gateways create - create a new Compute Engine Highly Available VPN gateway 
SYNOPSIS
    

`gcloud beta compute vpn-gateways create` `NAME` `--network`=`NETWORK` [`--description`=`DESCRIPTION`] [`--gateway-ip-version`=`GATEWAY_IP_VERSION`] [`--interconnect-attachments`=[`INTERCONNECT_ATTACHMENTS`,…]] [`--region`=`REGION`] [`--resource-manager-tags`=[`KEY`=`VALUE`,…]] [`--stack-type`=`STACK_TYPE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute vpn-gateways create` creates a new Highly Available VPN gateway. 

Highly Available VPN Gateway provides a means to create a VPN solution with a higher availability SLA compared to Classic Target VPN Gateway. Highly Available VPN gateways are simply referred to as VPN gateways in the API documentation and gcloud commands. A VPN Gateway can reference one or more VPN tunnels that connect it to external VPN gateways or Cloud VPN Gateways. 

EXAMPLES
     To create a VPN gateway, run: 
    
    
    gcloud beta compute vpn-gateways create my-vpn-gateway --region=us-central1 --network=default

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the VPN Gateway to create. 
REQUIRED FLAGS
    

`--network`=`NETWORK`
     A reference to a network to which the VPN gateway is attached. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     An optional, textual description for the VPN gateway. 
`--gateway-ip-version`=`GATEWAY_IP_VERSION`
     IP version of the HA VPN gateway. You must specify either IPv4 or IPv6. If you do not specify this field, every HA VPN gateway interface will be configured with an IPv4 address. `GATEWAY_IP_VERSION` must be one of: 

`IPV4`
     Every HA-VPN gateway interface is configured with an IPv4 address. 
`IPV6`
     Every HA-VPN gateway interface is configured with an IPv6 address. 
`--interconnect-attachments`=[`INTERCONNECT_ATTACHMENTS`,…]
     Names of interconnect attachments (VLAN attachments) associated with the VPN gateway interfaces. You must specify this field when using a VPN gateway for HA VPN over Cloud Interconnect. Otherwise, this field is optional. 

For example, `--interconnect-attachments attachment-a-zone1,attachment-a-zone2` associates VPN gateway with attachment from zone1 on interface 0 and with attachment from zone2 on interface 1\. 

`--region`=`REGION`
     Region of the VPN Gateway to create. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--resource-manager-tags`=[`KEY`=`VALUE`,…]
     A comma-separated list of Resource Manager tags to apply to the VPN gateway. 
`--stack-type`=`STACK_TYPE`
     The stack type of the protocol(s) enabled on this VPN gateway. If not provided, `IPV4_ONLY` will be used. `STACK_TYPE` must be one of: 

`IPV4_IPV6`
     Both IPv4 and IPv6 protocols are enabled on this VPN gateway. 
`IPV4_ONLY`
     Only IPv4 protocol is enabled on this VPN gateway. 
`IPV6_ONLY`
     Only IPv6 protocol is enabled on this VPN gateway. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute vpn-gateways create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways/create)
    
    
    [gcloud alpha compute vpn-gateways create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/vpn-gateways/create)
    
    
    [gcloud preview compute vpn-gateways create](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/vpn-gateways/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
