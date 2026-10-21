---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/runtime-config/configs/variables/watch/
title: gcloud beta runtime-config configs variables watch \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:32:59.602187+00:00
---

# gcloud beta runtime-config configs variables watch  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/runtime-config/configs/variables/watch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta runtime-config configs variables watch Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta runtime-config configs variables watch - wait for a variable resources to change 
SYNOPSIS
    

`gcloud beta runtime-config configs variables watch` `NAME` `--config-name`=`CONFIG_NAME` [`--max-wait`=`MAX_WAIT`] [`--newer-than`=`NEWER_THAN`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command waits for the variable resource with the specified name to either have its value changed or be deleted. 
EXAMPLES
     To wait for a variable to change or be deleted, run: 
    
    
    gcloud beta runtime-config configs variables watch my-var --config-name=my-config

This command will return after the variable changes, is deleted, or a server-defined timeout elapses. 

To wait for user-specified period of 20 seconds, run: 
    
    
    gcloud beta runtime-config configs variables watch my-var --config-name=my-config --max-wait=20

If a watch command returns due to a timeout, the command's exit value will be 2. All other errors result in an exit value of 1. If the watched variable changes prior to the timeout, the command will exit successfully with a value of 0. 

Optionally, a --newer-than parameter can be specified to wait only if the variable hasn't changed since the specified time. If the variable has changed since the time passed to --newer-than, the command returns without waiting. For example: 
    
    
    gcloud beta runtime-config configs variables watch my-var --config-name=my-config --newer-than="2016-04-05T12:00:00Z"

POSITIONAL ARGUMENTS
    

`NAME`
     Variable name. 
REQUIRED FLAGS
    

`--config-name`=`CONFIG_NAME`
     The name of the configuration resource to use. 
OPTIONAL FLAGS
    

`--max-wait`=`MAX_WAIT`
     An optional maximum time to wait. For example, "30s". See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
`--newer-than`=`NEWER_THAN`
     Return immediately if the stored variable is newer than this time. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
