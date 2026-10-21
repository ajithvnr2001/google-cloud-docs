---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/sub-blocks/report-subblock-as-faulty/
title: gcloud beta compute reservations sub-blocks report-subblock-as-faulty \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:41:21.551471+00:00
---

# gcloud beta compute reservations sub-blocks report-subblock-as-faulty  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/sub-blocks/report-subblock-as-faulty/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute reservations sub-blocks report-subblock-as-faulty Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute reservations sub-blocks report-subblock-as-faulty - report a sub-block within a reservation as faulty 
SYNOPSIS
    

`gcloud beta compute reservations sub-blocks report-subblock-as-faulty` `RESERVATION` `--block-name`=`BLOCK_NAME` `--disruption-schedule`=`DISRUPTION_SCHEDULE` `--failure-component`=`FAILURE_COMPONENT` `--fault-reasons`=[`behavior`=`BEHAVIOR`],[`description`=`DESCRIPTION`] `--sub-block-name`=`SUB_BLOCK_NAME` [`--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Report a sub-block within a reservation as faulty. 
EXAMPLES
     To report reservation exr-1 in ZONE with block name block-1 and sub block name sub-block-1 as faulty, run: 
    
    
    [gcloud beta compute reservations sub-blocks](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/sub-blocks) report-subblock-as-faulty exr-1 --zone=ZONE --block-name=block-1 --sub-block-name=sub-block-1 --disruption-schedule=IMMEDIATE --fault-reasons=behavior=PERFORMANCE,description="performance issues" --failure-component=NVLINK_SWITCH

POSITIONAL ARGUMENTS
    

`RESERVATION`
     The name of the reservation containing the sub-block to report as faulty 
REQUIRED FLAGS
    

`--block-name`=`BLOCK_NAME`
     The name of the reservation block. 
`--disruption-schedule`=`DISRUPTION_SCHEDULE`
     The disruption schedule for the sub-block. `DISRUPTION_SCHEDULE` must be (only one value is supported): 

`IMMEDIATE`
     All VMs are immediately disrupted. 
`--failure-component`=`FAILURE_COMPONENT`
     The component that experienced the fault. `FAILURE_COMPONENT` must be one of: 

`MULTIPLE_FAULTY_HOSTS`
     Multiple hosts experienced the fault. 
`NVLINK_SWITCH`
     The NVLink switch experienced the fault. 
`--fault-reasons`=[`behavior`=`BEHAVIOR`],[`description`=`DESCRIPTION`]
     The reasons for reporting the sub-block as faulty. You can repeat this flag. Each flag must specify a "behavior" attribute and can optionally include a "description" attribute. The possible values for "behavior" are: PERFORMANCE, SWITCH_FAILURE, GPU_ERROR. 
`--sub-block-name`=`SUB_BLOCK_NAME`
     The name of the reservation sub block. 
OPTIONAL FLAGS
    

`--zone`=`ZONE`
     Zone of the reservation to report-subblock-as-faulty. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

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
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute reservations sub-blocks report-subblock-as-faulty](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/sub-blocks/report-subblock-as-faulty)
    
    
    [gcloud alpha compute reservations sub-blocks](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/reservations/sub-blocks) report-subblock-as-faulty
    
    
    [gcloud preview compute reservations sub-blocks](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/reservations/sub-blocks) report-subblock-as-faulty

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
