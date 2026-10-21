---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/get-nat-ip-info/
title: gcloud compute routers get-nat-ip-info \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:52:47.919071+00:00
---

# gcloud compute routers get-nat-ip-info  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/get-nat-ip-info/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute routers get-nat-ip-info Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute routers get-nat-ip-info - display NAT IP information in a router 
SYNOPSIS
    

`gcloud compute routers get-nat-ip-info` `NAME` [`--nat-name`=`NAT_NAME`] [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
    
    
    
    gcloud compute routers get-nat-ip-info

shows a mapping of IP:[usage, mode] allocated to each NAT via the specified router. 

EXAMPLES
     To show NAT IP information from all NATs in router 'r1' in region 'us-central1', run: 
    
    
    gcloud compute routers get-nat-ip-info r1 --region=us-central1

To show NAT IP information for a specific NAT 'nat1' in router 'r1' in region 'us-central1', run: 
    
    
    gcloud compute routers get-nat-ip-info r1 --region=us-central1 --nat-name="nat1"

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the router to get NAT IP info. 
FLAGS
    

`--nat-name`=`NAT_NAME`
     The NAT name to filter out NAT IP information 
`--region`=`REGION`
     Region of the router to get NAT IP info. If not specified, you might be prompted to select a region (interactive mode only). 

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
    
    
    [gcloud alpha compute routers get-nat-ip-info](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/routers/get-nat-ip-info)
    
    
    [gcloud beta compute routers get-nat-ip-info](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/routers/get-nat-ip-info)
    
    
    [gcloud preview compute routers get-nat-ip-info](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/routers/get-nat-ip-info)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
