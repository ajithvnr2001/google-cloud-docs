---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/public-delegated-prefixes/create/
title: gcloud beta compute public-delegated-prefixes create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:06:54.567392+00:00
---

# gcloud beta compute public-delegated-prefixes create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/public-delegated-prefixes/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute public-delegated-prefixes create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute public-delegated-prefixes create - creates a Compute Engine public delegated prefix 
SYNOPSIS
    

`gcloud beta compute public-delegated-prefixes create` `NAME` `--range`=`RANGE` (`--public-advertised-prefix`=`PUBLIC_ADVERTISED_PREFIX` | `--public-delegated-prefix`=`PUBLIC_DELEGATED_PREFIX`) [`--allocatable-prefix-length`=`ALLOCATABLE_PREFIX_LENGTH`] [`--description`=`DESCRIPTION`] [`--enable-live-migration`] [`--mode`=`MODE`] [`--purpose`=`PURPOSE`] [`--global` | `--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To create a public delegated prefix: 
    
    
    gcloud beta compute public-delegated-prefixes create my-public-delegated-prefix --public-advertised-prefix=my-pap --range=120.120.10.128/27 --global

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the public delegated prefix to operate on. 
REQUIRED FLAGS
    

`--range`=`RANGE`
     IP range from this public delegated prefix that should be delegated, in CIDR format. It must be smaller than parent public advertised prefix range. 
Exactly one of these must be specified: 

`--public-advertised-prefix`=`PUBLIC_ADVERTISED_PREFIX`
     Public advertised prefix that this delegated prefix is created from. 
`--public-delegated-prefix`=`PUBLIC_DELEGATED_PREFIX`
     Regional Public delegated prefix that this delegated prefix is created from. 
OPTIONAL FLAGS
    

`--allocatable-prefix-length`=`ALLOCATABLE_PREFIX_LENGTH`
     The allocatable prefix length supported by this PDP. 
`--description`=`DESCRIPTION`
     Description of this public delegated prefix. 
`--enable-live-migration`
     Specify if this public delegated prefix is meant to be live migrated. 
`--mode`=`MODE`
     Specifies the mode of this IPv6 PDP. `MODE` must be one of: `delegation`, `external-ipv6-forwarding-rule-creation`, `external-ipv6-subnetwork-creation`, `internal-ipv6-subnetwork-creation`. 
`--purpose`=`PURPOSE`
     The purpose of the public delegated prefix. This field can only be set for the top-level global public delegated prefix. `PURPOSE` must be one of: `APPLICATION_AND_PROXY_LOAD_BALANCERS`, `PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP0`, `PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP1`. 
At most one of these can be specified: 

`--global`
     If set, the public delegated prefix is global. 
`--region`=`REGION`
     Region of the public delegated prefix to operate on. Overrides the default `compute/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute public-delegated-prefixes create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/create)
    
    
    [gcloud alpha compute public-delegated-prefixes create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/public-delegated-prefixes/create)
    
    
    [gcloud preview compute public-delegated-prefixes create](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/public-delegated-prefixes/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
