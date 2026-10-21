---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/commitments/describe/
title: gcloud compute commitments describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:08:05.480496+00:00
---

# gcloud compute commitments describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/commitments/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute commitments describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute commitments describe - describe a Compute Engine commitment 
SYNOPSIS
    

`gcloud compute commitments describe` `COMMITMENT` [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute commitments describe` displays all data associated with a Compute Engine resource-based commitment. 

Note that the memory capacity returned by this command is in MB (where 1 MB = 2^20 bytes, equivalent to MiB). 

In contrast, the `[gcloud compute commitments create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/commitments/create)` command and the Web Console default to GB (where 1 GB = 2^30 bytes, equivalent to GiB). If you plan to repurchase commitments for your resources by using the Google Cloud console or the `[gcloud compute commitments create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/commitments/create)` command, then don't reuse the memory numbers directly from the output of the `describe` command. Make sure to convert the memory amount to GB first. Otherwise, you end up purchasing a commitment for 1024 times the intended amount. 

Local SSD capacity, however, is consistently measured in GB across both `describe` and `create` commands. 

EXAMPLES
     To describe the commitment called ``commitment-1`` in the ``us-central1`` region, run: 
    
    
    gcloud compute commitments describe commitment-1 --region=us-central1

POSITIONAL ARGUMENTS
    

`COMMITMENT`
     Name of the commitment to describe. 
FLAGS
    

`--region`=`REGION`
     Region of the commitment to describe. If not specified, you might be prompted to select a region (interactive mode only). 

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
    
    
    [gcloud alpha compute commitments describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/describe)
    
    
    [gcloud beta compute commitments describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/commitments/describe)
    
    
    [gcloud preview compute commitments describe](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/commitments/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
