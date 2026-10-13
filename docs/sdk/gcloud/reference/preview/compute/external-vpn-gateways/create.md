---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/external-vpn-gateways/create/
title: gcloud preview compute external-vpn-gateways create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:54.421500+00:00
---

# gcloud preview compute external-vpn-gateways create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/external-vpn-gateways/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute external-vpn-gateways create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute external-vpn-gateways create - create a new Compute Engine external VPN gateway 
SYNOPSIS
    

`gcloud preview compute external-vpn-gateways create` `NAME` `--interfaces`=[`ID`=`IP_ADDRESS`,…] [`--description`=`DESCRIPTION`] [`--resource-manager-tags`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute external-vpn-gateways create` creates a new external VPN gateway. 

External VPN gateway is the on-premises VPN gateway or another cloud provider's VPN gateway that connects to your Google Cloud VPN gateway. To create a highly available VPN from Google Cloud to your on-premises side or another Cloud provider's VPN gateway, you must create an external VPN gateway resource in Google Cloud, which provides the information to Google Cloud about your external VPN gateway. 

EXAMPLES
     To create an external VPN gateway, run: 
    
    
    gcloud preview compute external-vpn-gateways create my-external-gateway --interfaces=0=8.9.9.9

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the external VPN gateway to create. 
REQUIRED FLAGS
    

`--interfaces`=[`ID`=`IP_ADDRESS`,…]
     Map of interfaces from interface ID to interface IP address for the External VPN Gateway. 

There can be one, two, or four interfaces in the map. 

For example, to create an external VPN gateway with one interface: 
    
    
    gcloud preview compute external-vpn-gateways create MY-EXTERNAL-GATEWAY --interfaces 0=192.0.2.0

To create an external VPN gateway with two interfaces: $ gcloud preview compute external-vpn-gateways create \ MY-EXTERNAL-GATEWAY --interfaces 0=192.0.2.0,1=192.0.2.1 

To create an external VPN gateway with four interfaces: $ gcloud preview compute external-vpn-gateways create \ MY-EXTERNAL-GATEWAY \ --interfaces 0=192.0.2.0,1=192.0.2.1,2=192.0.2.3,3=192.0.2.4 

To create an external VPN gateway with IPv6 addresses on four interfaces: $ gcloud preview compute external-vpn-gateways create \ MY-EXTERNAL-GATEWAY \ \--interfaces \ 0=2001:db8::1,1=2001:db8::2,2=2001:db8::3,3=2001:db8::4 

Note that the redundancy type of the gateway will be automatically inferred based on the number of interfaces provided: 
    
    
    1 interface: `SINGLE_IP_INTERNALLY_REDUNDANT`
    
    
    2 interfaces: `TWO_IPS_REDUNDANCY`
    
    
    4 interfaces: `FOUR_IPS_REDUNDANCY`

OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     Textual description of the External VPN Gateway. 
`--resource-manager-tags`=[`KEY`=`VALUE`,…]
     A comma-separated list of Resource Manager tags to apply to the external VPN gateway. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute external-vpn-gateways create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/external-vpn-gateways/create)
    
    
    [gcloud alpha compute external-vpn-gateways create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/external-vpn-gateways/create)
    
    
    [gcloud beta compute external-vpn-gateways create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/external-vpn-gateways/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
