---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/networks/subnets/expand-ip-range/
title: gcloud alpha compute networks subnets expand-ip-range \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:17:33.019229+00:00
---

# gcloud alpha compute networks subnets expand-ip-range  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/networks/subnets/expand-ip-range/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute networks subnets expand-ip-range Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute networks subnets expand-ip-range - expand the IP range of a Compute Engine subnetwork 
SYNOPSIS
    

`gcloud alpha compute networks subnets expand-ip-range` `NAME` `--prefix-length`=`PREFIX_LENGTH` [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute networks subnets expand-ip-range` expands the IP range of a VPC subnetwork. 

For more information about expanding a subnet, see [Expanding a primary IP range](https://cloud.google.com/vpc/docs/using-vpc#expand-subnet). 

This command doesn't work for secondary subnets or for subnets that are used exclusively for load balancer proxies. For more information, see [Proxy-only subnets for load balancers](https://cloud.google.com/load-balancing/docs/l7-internal/proxy-only-subnets). 

EXAMPLES
     To expand the IP range of ``SUBNET`` to /16, run: 
    
    
    gcloud alpha compute networks subnets expand-ip-range SUBNET --region=us-central1 --prefix-length=16

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the subnetwork to operate on. 
REQUIRED FLAGS
    

`--prefix-length`=`PREFIX_LENGTH`
     The new prefix length of the subnet. It must be smaller than the original and in the private address space 10.0.0.0/8, 172.16.0.0/12 or 192.168.0.0/16 defined in RFC 1918. 
OPTIONAL FLAGS
    

`--region`=`REGION`
     Region of the subnetwork to operate on. If not specified, you might be prompted to select a region (interactive mode only). 

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
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute networks subnets expand-ip-range](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/expand-ip-range)
    
    
    [gcloud beta compute networks subnets expand-ip-range](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/networks/subnets/expand-ip-range)
    
    
    [gcloud preview compute networks subnets expand-ip-range](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/networks/subnets/expand-ip-range)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
