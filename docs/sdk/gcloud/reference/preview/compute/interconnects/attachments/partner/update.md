---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/attachments/partner/update/
title: gcloud preview compute interconnects attachments partner update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:07:17.196283+00:00
---

# gcloud preview compute interconnects attachments partner update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/attachments/partner/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute interconnects attachments partner update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute interconnects attachments partner update - update a Compute Engine partner interconnect attachment 
SYNOPSIS
    

`gcloud preview compute interconnects attachments partner update` `NAME` [`--candidate-cloud-router-ipv6-address`=`CANDIDATE_CLOUD_ROUTER_IPV6_ADDRESS`] [`--candidate-customer-router-ipv6-address`=`CANDIDATE_CUSTOMER_ROUTER_IPV6_ADDRESS`] [`--description`=`DESCRIPTION`] [`--enable-admin`] [`--mtu`=`MTU`] [`--region`=`REGION`] [`--stack-type`=`STACK_TYPE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute interconnects attachments partner update` is used to update partner interconnect attachments. A partner interconnect attachment binds the underlying connectivity of a provider's Interconnect to a path into and out of the customer's cloud network. 
POSITIONAL ARGUMENTS
    

`NAME`
     Name of the interconnect attachment to patch. 
FLAGS
    

`--candidate-cloud-router-ipv6-address`=`CANDIDATE_CLOUD_ROUTER_IPV6_ADDRESS`
     Single IPv6 address + prefix length to be configured on the cloud router interface for this interconnect attachment. Example: 2001:db8::1/125 
`--candidate-customer-router-ipv6-address`=`CANDIDATE_CUSTOMER_ROUTER_IPV6_ADDRESS`
     Single IPv6 address + prefix length to be configured on the customer router interface for this interconnect attachment. Example: 2001:db8::2/125 
`--description`=`DESCRIPTION`
     Human-readable plain-text description of attachment. 
`--enable-admin`
     Administrative status of the interconnect attachment. When this is enabled, the attachment is operational and will carry traffic. Use --no-enable-admin to disable it. 
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

`--stack-type`=`STACK_TYPE`
     Stack type of the protocol(s) enabled on this interconnect attachment. `STACK_TYPE` must be one of: 

`IPV4_IPV6`
     Both IPv4 and IPv6 protocols are enabled on this attachment. 
`IPV4_ONLY`
     Only IPv4 protocol is enabled on this attachment. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute interconnects attachments partner update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/update)
    
    
    [gcloud alpha compute interconnects attachments partner update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/partner/update)
    
    
    [gcloud beta compute interconnects attachments partner update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/attachments/partner/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
