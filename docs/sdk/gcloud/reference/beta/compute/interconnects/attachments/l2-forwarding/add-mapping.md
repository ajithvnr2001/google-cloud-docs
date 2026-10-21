---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/attachments/l2-forwarding/add-mapping/
title: gcloud beta compute interconnects attachments l2-forwarding add-mapping \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:49:22.544046+00:00
---

# gcloud beta compute interconnects attachments l2-forwarding add-mapping  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/attachments/l2-forwarding/add-mapping/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute interconnects attachments l2-forwarding add-mapping Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute interconnects attachments l2-forwarding add-mapping - add new vlan to ip mapping rule to an L2-forwarding attachment 
SYNOPSIS
    

`gcloud beta compute interconnects attachments l2-forwarding add-mapping` `NAME` `--vlan-key`=`VLAN_KEY` [`--appliance-ip-address`=`ADDRESSES`] [`--appliance-name`=`APPLIANCE_NAME`] [`--inner-vlan-to-appliance-mappings`=[`innerApplianceIpAddress`=`INNERAPPLIANCEIPADDRESS`],[`innerVlanTags`=`INNERVLANTAGS`]] [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute interconnects attachments l2-forwarding add-mapping` add new vlan to ip mapping rule to an L2-forwarding attachment. 
POSITIONAL ARGUMENTS
    

`NAME`
     Name of the interconnect attachment to patch. 
REQUIRED FLAGS
    

`--vlan-key`=`VLAN_KEY`
     Desired VLAN key for L2 forwarding mapping for the attachment. If not supplied, all mappings will be displayed. 
OPTIONAL FLAGS
    

`--appliance-ip-address`=`ADDRESSES`
     A single IPv4 or IPv6 address used as the destination IP address for ingress packets that match on a VLAN tag, but do not match a more specific inner VLAN tag. 
`--appliance-name`=`APPLIANCE_NAME`
     The name of the L2 appliance mapping rule. 
`--inner-vlan-to-appliance-mappings`=[`innerApplianceIpAddress`=`INNERAPPLIANCEIPADDRESS`],[`innerVlanTags`=`INNERVLANTAGS`]
     A list of mapping rules from inner VLAN tags to IP addresses. If the inner VLAN is not explicitly mapped to an IP address range, the applianceIpAddress is used. 
`--region`=`REGION`
     Region of the interconnect attachment to patch. If not specified, you might be prompted to select a region (interactive mode only). 

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
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute interconnects attachments l2-forwarding add-mapping](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/l2-forwarding/add-mapping)
    
    
    [gcloud alpha compute interconnects attachments l2-forwarding](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/l2-forwarding) add-mapping
    
    
    [gcloud preview compute interconnects attachments l2-forwarding](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/attachments/l2-forwarding) add-mapping

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
