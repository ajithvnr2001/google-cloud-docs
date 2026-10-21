---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/public-delegated-prefixes/delegated-sub-prefixes/create/
title: gcloud beta compute public-delegated-prefixes delegated-sub-prefixes create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:41:32.254999+00:00
---

# gcloud beta compute public-delegated-prefixes delegated-sub-prefixes create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/public-delegated-prefixes/delegated-sub-prefixes/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute public-delegated-prefixes delegated-sub-prefixes create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute public-delegated-prefixes delegated-sub-prefixes create - creates a Compute Engine delegated sub prefix 
SYNOPSIS
    

`gcloud beta compute public-delegated-prefixes delegated-sub-prefixes create` `NAME` `--public-delegated-prefix`=`PUBLIC_DELEGATED_PREFIX` [`--allocatable-prefix-length`=`ALLOCATABLE_PREFIX_LENGTH`] [`--create-addresses`] [`--delegatee-project`=`DELEGATEE_PROJECT`] [`--description`=`DESCRIPTION`] [`--mode`=`MODE`] [`--range`=`RANGE`] [`--global-public-delegated-prefix` | `--public-delegated-prefix-region`=`PUBLIC_DELEGATED_PREFIX_REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Creates a Compute Engine delegated sub prefix. 
EXAMPLES
     To create a delegated sub prefix for a global public delegated prefix: 
    
    
    [gcloud beta compute public-delegated-prefixes](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/public-delegated-prefixes) delegated-sub-prefixes create my-sub-prefix --range=120.120.10.128/28 --public-delegated-prefix=my-pdp --global-public-delegated-prefix

To create a delegated sub prefix for a regional public delegated prefix: 
    
    
    [gcloud beta compute public-delegated-prefixes](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/public-delegated-prefixes) delegated-sub-prefixes create my-sub-prefix --range=120.120.10.128/30 --create-addresses --public-delegated-prefix=my-pdp --public-delegated-prefix-region=us-east1

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the delegated sub prefix to create. 
REQUIRED FLAGS
    

`--public-delegated-prefix`=`PUBLIC_DELEGATED_PREFIX`
     Name of the public delegated prefix to create the delegate sub prefix for. 
OPTIONAL FLAGS
    

`--allocatable-prefix-length`=`ALLOCATABLE_PREFIX_LENGTH`
     Specify allocatable prefix length supported by this sub prefix. 
`--create-addresses`
     Specify if the sub prefix is delegated to create address resources in the delegatee project. Default is false. 
`--delegatee-project`=`DELEGATEE_PROJECT`
     Project to delegate the IPv4 range specified in `--range` to. If empty, the sub-range is delegated to the same/existing project. 
`--description`=`DESCRIPTION`
     Description of the delegated sub prefix to create. 
`--mode`=`MODE`
     Specifies the mode of this IPv6 PDP. `MODE` must be one of: `delegation`, `external-ipv6-forwarding-rule-creation`, `external-ipv6-subnetwork-creation`, `internal-ipv6-subnetwork-creation`. 
`--range`=`RANGE`
     IPv4 range from this public delegated prefix that should be delegated, in CIDR format. If not specified, the entire range ofthe public advertised prefix is delegated. 
At most one of these can be specified: 

`--global-public-delegated-prefix`
     If set, the public delegated prefix is global. 
`--public-delegated-prefix-region`=`PUBLIC_DELEGATED_PREFIX_REGION`
     Region of the public delegated prefix to create the delegate sub prefix for. If not specified, you might be prompted to select a region (interactive mode only). 

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
    
    
    [gcloud compute public-delegated-prefixes delegated-sub-prefixes](https://docs.cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes) create
    
    
    [gcloud alpha compute public-delegated-prefixes](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/public-delegated-prefixes) delegated-sub-prefixes create
    
    
    [gcloud preview compute public-delegated-prefixes](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/public-delegated-prefixes) delegated-sub-prefixes create

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
