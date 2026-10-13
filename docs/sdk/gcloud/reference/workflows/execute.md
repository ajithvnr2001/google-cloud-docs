---
url: https://docs.cloud.google.com/sdk/gcloud/reference/workflows/execute/
title: gcloud workflows execute \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:32.874363+00:00
---

# gcloud workflows execute  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/workflows/execute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud workflows execute Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud workflows execute - execute a workflow 
SYNOPSIS
    

`gcloud workflows execute` (`WORKFLOW` : `--location`=`LOCATION`) [`--call-log-level`=`CALL_LOG_LEVEL`; default="none"] [`--data`=`DATA`] [`--disable-concurrency-quota-overflow-buffering`] [`--execution-history-level`=`EXECUTION_HISTORY_LEVEL`; default="none"] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Execute a workflow. 
EXAMPLES
     To execute a workflow named 'my-workflow' with the data that will be passed to the workflow, run: 
    
    
    gcloud workflows execute my-workflow --data=my-data

POSITIONAL ARGUMENTS
    

Workflow resource - Name of the workflow to execute. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `workflow` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`WORKFLOW`
     ID of the workflow or fully qualified identifier for the workflow. 

To set the `workflow` attribute: 

  * provide the argument `workflow` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The Cloud location for the workflow. Alternatively, set the property [workflows/location]. To set the `location` attribute: 

  * provide the argument `workflow` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `workflows/location`. 


FLAGS
    

`--call-log-level`=`CALL_LOG_LEVEL`; default="none"
     Level of call logging to apply during execution. `CALL_LOG_LEVEL` must be one of: 

`log-all-calls`
     Log all calls to subworkflows or library functions and their results. 
`log-errors-only`
     Log when a call is stopped due to an exception. 
`log-none`
     Perform no call logging. 
`none`
     No call logging level specified. 
`--data`=`DATA`
     JSON string with data that will be passed to the workflow as an argument. 
`--disable-concurrency-quota-overflow-buffering`
     If set, the execution will not be backlogged when the concurrency quota is exhausted. Backlogged executions start when the concurrency quota becomes available. 
`--execution-history-level`=`EXECUTION_HISTORY_LEVEL`; default="none"
     Level of execution history to apply during execution. `EXECUTION_HISTORY_LEVEL` must be one of: 

`execution-history-basic`
     Enable basic execution history. 
`execution-history-detailed`
     Enable detailed execution history, including expected iterations and in-scope variable values. 
`none`
     No execution history level specified. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens, underscores, lowercase characters, and numbers. Values must contain only hyphens, underscores, lowercase characters, and numbers. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `workflowexecutions/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/workflows>
NOTES
     This variant is also available: 
    
    
    [gcloud beta workflows execute](https://docs.cloud.google.com/sdk/gcloud/reference/beta/workflows/execute)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
