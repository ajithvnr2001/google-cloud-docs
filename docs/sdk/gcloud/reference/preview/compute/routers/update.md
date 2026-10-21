---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/routers/update/
title: gcloud preview compute routers update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:01:52.311181+00:00
---

# gcloud preview compute routers update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/routers/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute routers update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute routers update - update a Compute Engine router 
SYNOPSIS
    

`gcloud preview compute routers update` `NAME` [`--advertisement-mode`=`MODE`] [`--asn`=`ASN`] [`--async`] [`--bgp-identifier-range`=`BGP_IDENTIFIER_RANGE`] [`--keepalive-interval`=`KEEPALIVE_INTERVAL`] [`--region`=`REGION`] [`--set-advertisement-groups`=[`GROUP`,…]] [`--set-advertisement-ranges`=[`CIDR_RANGE`=`DESC`,…]] [`--add-advertisement-groups`=[`GROUP`,…] | `--add-advertisement-ranges`=[`CIDR_RANGE`=`DESC`,…] | `--remove-advertisement-groups`=[`GROUP`,…] | `--remove-advertisement-ranges`=[`CIDR_RANGE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute routers update` is used to update a Compute Engine router. 
POSITIONAL ARGUMENTS
    

`NAME`
     Name of the router to update. 
FLAGS
    

`--advertisement-mode`=`MODE`
     The new advertisement mode for this router. `MODE` must be one of: 

`CUSTOM`
     Custom (user-configured) BGP advertisements. 
`DEFAULT`
     Default (Google-managed) BGP advertisements. 
`--asn`=`ASN`
     The optional BGP autonomous system number (ASN) for this router. Must be a 16-bit or 32-bit private ASN as defined in https://tools.ietf.org/html/rfc6996, for example `--asn=64512`. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--bgp-identifier-range`=`BGP_IDENTIFIER_RANGE`
     The range of valid BGP Identifiers for this Router. Must be a link-local IPv4 range from 169.254.0.0/16, of size at least /30, even if the BGP sessions are over IPv6. It must not overlap with any IPv4 BGP session ranges. This is commonly called "router ID" by other vendors. 
`--keepalive-interval`=`KEEPALIVE_INTERVAL`
     The interval between BGP keepalive messages that are sent to the peer. If set, this value must be between 20 and 60 seconds. The default is 20 seconds. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 

BGP systems exchange keepalive messages to determine whether a link or host has failed or is no longer available. Hold time is the length of time in seconds that the BGP session is considered operational without any activity. After the hold time expires, the session is dropped. 

Hold time is three times the interval at which keepalive messages are sent, and the hold time is the maximum number of seconds allowed to elapse between successive keepalive messages that BGP receives from a peer. BGP will use the smaller of either the local hold time value or the peer's hold time value as the hold time for the BGP connection between the two peers. 

`--region`=`REGION`
     Region of the router to update. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--set-advertisement-groups`=[`GROUP`,…]
     The list of pre-defined groups of IP ranges to dynamically advertise on this router. This list can only be specified in custom advertisement mode. 

`GROUP` must be (only one value is supported): 

`ALL_SUBNETS`
     Automatically advertise all available subnets. This excludes any routes learned for subnets that use VPC Network Peering. 
`--set-advertisement-ranges`=[`CIDR_RANGE`=`DESC`,…]
     The list of individual IP ranges, in CIDR format, to dynamically advertise on this router. Each IP range can (optionally) be given a text description DESC. For example, to advertise a specific range, use `--set-advertisement-ranges=192.168.10.0/24`. To store a description with the range, use `--set-advertisement-ranges=192.168.10.0/24=my-networks`. This list can only be specified in custom advertisement mode. 
At most one of these can be specified: 

`--add-advertisement-groups`=[`GROUP`,…]
     A list of pre-defined groups of IP ranges to dynamically advertise on this router. This list is appended to any existing advertisements. This field can only be specified in custom advertisement mode. 

`GROUP` must be (only one value is supported): 

`ALL_SUBNETS`
     Automatically advertise all available subnets. This excludes any routes learned for subnets that use VPC Network Peering. 
`--add-advertisement-ranges`=[`CIDR_RANGE`=`DESC`,…]
     A list of individual IP ranges, in CIDR format, to dynamically advertise on this router. This list is appended to any existing advertisements. Each IP range can (optionally) be given a text description DESC. For example, to advertise a specific range, use `--advertisement-ranges=192.168.10.0/24`. To store a description with the range, use `--advertisement-ranges=192.168.10.0/24=my-networks`. This list can only be specified in custom advertisement mode. 
`--remove-advertisement-groups`=[`GROUP`,…]
     A list of pre-defined groups of IP ranges to remove from dynamic advertisement on this router. Each group in the list must exist in the current set of custom advertisements. This field can only be specified in custom advertisement mode. 

`GROUP` must be (only one value is supported): 

`ALL_SUBNETS`
     Automatically advertise all available subnets. This excludes any routes learned for subnets that use VPC Network Peering. 
`--remove-advertisement-ranges`=[`CIDR_RANGE`,…]
     A list of individual IP ranges, in CIDR format, to remove from dynamic advertisement on this router. Each IP range in the list must exist in the current set of custom advertisements. This field can only be specified in custom advertisement mode. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute routers update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/update)
    
    
    [gcloud alpha compute routers update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/routers/update)
    
    
    [gcloud beta compute routers update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/routers/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
