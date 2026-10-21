---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/report-host-as-faulty/
title: gcloud preview compute instances report-host-as-faulty \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:44:08.034322+00:00
---

# gcloud preview compute instances report-host-as-faulty  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/report-host-as-faulty/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute instances report-host-as-faulty Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute instances report-host-as-faulty - report a host as faulty to start the repair process 
SYNOPSIS
    

`gcloud preview compute instances report-host-as-faulty` `INSTANCE_NAME` `--disruption-schedule`=`DISRUPTION_SCHEDULE` `--fault-reasons`=[`behavior`=`BEHAVIOR`],[`description`=`DESCRIPTION`] [`--async`] [`--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute instances report-host-as-faulty` is used to report a host as faulty to start the repair process. 
EXAMPLES
     To report a host as faulty for an instance named ``test-instance``, run: 
    
    
    gcloud preview compute instances report-host-as-faulty test-instance --fault-reasons=behavior=SILENT_DATA_CORRUPTION,description="affecting our ML job" --disruption-schedule=IMMEDIATE

POSITIONAL ARGUMENTS
    

`INSTANCE_NAME`
     Name of the instance to operate on. For details on valid instance names, refer to the criteria documented under the field 'name' at: <https://cloud.google.com/compute/docs/reference/rest/v1/instances>
REQUIRED FLAGS
    

`--disruption-schedule`=`DISRUPTION_SCHEDULE`
     Specifies the timing for initiating the fault reporting process. The default value is IMMEDIATE which initiates the process right away. `DISRUPTION_SCHEDULE` must be one of: `IMMEDIATE`, `FUTURE`. 
`--fault-reasons`=[`behavior`=`BEHAVIOR`],[`description`=`DESCRIPTION`]
     Specified and can include one or more of the following types: ['BEHAVIOR_UNSPECIFIED', 'PERFORMANCE', 'SILENT_DATA_CORRUPTION', 'UNRECOVERABLE_GPU_ERROR', 'CHIP_ERROR']. This helps categorize the nature of the fault being reported. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--zone`=`ZONE`
     Zone of the instance to operate on. If not specified, you might be prompted to select a zone (interactive mode only). `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` attempts to identify the appropriate zone by searching for resources in your currently active project. If the zone cannot be determined, `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with all available Google Cloud Platform zones. 

To avoid prompting when this flag is omitted, the user can set the ``compute/zone`` property: 
    
    
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
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute instances report-host-as-faulty](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/report-host-as-faulty)
    
    
    [gcloud alpha compute instances report-host-as-faulty](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/report-host-as-faulty)
    
    
    [gcloud beta compute instances report-host-as-faulty](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/report-host-as-faulty)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
