---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/slots/get-version/
title: gcloud compute reservations slots get-version \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:24:38.170955+00:00
---

# gcloud compute reservations slots get-version  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/slots/get-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute reservations slots get-version Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute reservations slots get-version - get the version of a reservation slot 
SYNOPSIS
    

`gcloud compute reservations slots get-version` `RESERVATION` `--block-name`=`BLOCK_NAME` `--slot-name`=`SLOT_NAME` `--sub-block-name`=`SUB_BLOCK_NAME` [`--current`] [`--target`] [`--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Get the version of a reservation slot. 
EXAMPLES
     To get the current version of a reservation slot in reservation exr-1 in ZONE with block name block-1, sub-block name sub-block-1 and slot name slot-1, run: 
    
    
    gcloud compute reservations slots get-version exr-1 --zone=ZONE --block-name=block-1 --sub-block-name=sub-block-1 --slot-name=slot-1 --current

POSITIONAL ARGUMENTS
    

`RESERVATION`
     Name of the reservation to get-version. 
REQUIRED FLAGS
    

`--block-name`=`BLOCK_NAME`
     The name of the reservation block. 
`--slot-name`=`SLOT_NAME`
     The name of the reservation slot. 
`--sub-block-name`=`SUB_BLOCK_NAME`
     The name of the reservation sub block. 
OPTIONAL FLAGS
    

`--current`
     Whether to get the current version. 
`--target`
     Whether to get the target version. 
`--zone`=`ZONE`
     Zone of the reservation to get-version. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute reservations slots get-version](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/reservations/slots/get-version)
    
    
    [gcloud beta compute reservations slots get-version](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/slots/get-version)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
