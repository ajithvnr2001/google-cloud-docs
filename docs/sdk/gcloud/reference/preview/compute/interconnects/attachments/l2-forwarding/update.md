---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/attachments/l2-forwarding/update/
title: gcloud preview compute interconnects attachments l2-forwarding update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:38:25.344837+00:00
---

# gcloud preview compute interconnects attachments l2-forwarding update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/attachments/l2-forwarding/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute interconnects attachments l2-forwarding update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute interconnects attachments l2-forwarding update - update a Compute Engine L2 forwarding interconnect attachment 
SYNOPSIS
    

`gcloud preview compute interconnects attachments l2-forwarding update` `NAME` [`--bandwidth`=`BANDWIDTH`] [`--default-appliance-ip-address`=`DEFAULT_APPLIANCE_IP_ADDRESS`] [`--description`=`DESCRIPTION`] [`--enable-admin`] [`--geneve-vni`=`GENEVE_HEADER`] [`--mtu`=`MTU`] [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute interconnects attachments l2-forwarding update` is used to update interconnect attachments. An interconnect attachment is what binds the underlying connectivity of an interconnect to a path into and out of the customer's cloud network. 
POSITIONAL ARGUMENTS
    

`NAME`
     Name of the interconnect attachment to patch. 
FLAGS
    

`--bandwidth`=`BANDWIDTH`
     Provisioned capacity of the attachment. `BANDWIDTH` must be one of: 

`50m`
     50 Mbit/s 
`100m`
     100 Mbit/s 
`200m`
     200 Mbit/s 
`300m`
     300 Mbit/s 
`400m`
     400 Mbit/s 
`500m`
     500 Mbit/s 
`1g`
     1 Gbit/s 
`2g`
     2 Gbit/s 
`5g`
     5 Gbit/s 
`10g`
     10 Gbit/s 
`20g`
     20 Gbit/s 
`50g`
     50 Gbit/s 
`100g`
     100 Gbit/s 
`--default-appliance-ip-address`=`DEFAULT_APPLIANCE_IP_ADDRESS`
     A single IPv4 or IPv6 address used as the default destination IP when there is no VLAN mapping result found for L2 forwarding. Unset field indicates the unmatched packet should be dropped. 
`--description`=`DESCRIPTION`
     Human-readable plain-text description of attachment. 
`--enable-admin`
     Administrative status of the interconnect attachment. If not provided on creation, defaults to enabled. When this is enabled, the attachment is operational and will carry traffic. Use --no-enable-admin to disable it. 
`--geneve-vni`=`GENEVE_HEADER`
     A VNI identier for Geneve header, as defined in https://datatracker.ietf.org/doc/html/rfc8926, used for L2 forwarding. 
`--mtu`=`MTU`
     Maximum transmission unit (MTU) is the size of the largest IP packet passing through this interconnect attachment. Must be one of 1440, 1460, 1500, or 8896. If not specified, the value will default to 1440. 
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
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute interconnects attachments l2-forwarding update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/l2-forwarding/update)
    
    
    [gcloud alpha compute interconnects attachments l2-forwarding update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/l2-forwarding/update)
    
    
    [gcloud beta compute interconnects attachments l2-forwarding update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/attachments/l2-forwarding/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
