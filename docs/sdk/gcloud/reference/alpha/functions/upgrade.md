---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/functions/upgrade/
title: gcloud alpha functions upgrade \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:05.231945+00:00
---

# gcloud alpha functions upgrade  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/functions/upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha functions upgrade Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha functions upgrade - upgrade a 1st gen Cloud Function to the Cloud Run function 
SYNOPSIS
    

`gcloud alpha functions upgrade` (`NAME` : `--region`=`REGION`) [`--abort` | `--redirect-traffic` | `--rollback-traffic` | `--commit` `--skip-detach` | `--max-instances`=`MAX_INSTANCES` `--runtime`=`RUNTIME` `--setup-config` `--trigger-service-account`=`TRIGGER_SERVICE_ACCOUNT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Upgrade a 1st gen Cloud Function to the Cloud Run function. 
EXAMPLES
     To start the upgrade process for a 1st gen function `foo` and create a Cloud Run function copy, run: 
    
    
    gcloud alpha functions upgrade foo --setup-config

Once you are ready to redirect traffic to the Cloud Run function copy, run: 
    
    
    gcloud alpha functions upgrade foo --redirect-traffic

If you find you need to do more local testing you can rollback traffic to the 1st gen copy: 
    
    
    gcloud alpha functions upgrade foo --rollback-traffic

Once you're ready to finish upgrading and delete the 1st gen copy, run: 
    
    
    gcloud alpha functions upgrade foo --commit

You can abort the upgrade process at any time by running: 
    
    
    gcloud alpha functions upgrade foo --abort

POSITIONAL ARGUMENTS
    

Function resource - The Cloud Function name to upgrade. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `NAME` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`NAME`
     ID of the function or fully qualified identifier for the function. 

To set the `function` attribute: 

  * provide the argument `NAME` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The Cloud region for the function. Overrides the default `functions/region` property value for this command invocation. 

To set the `region` attribute: 

  * provide the argument `NAME` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `functions/region`. 


FLAGS
    

Upgrade a 1st gen Cloud Function to a Cloud Run Function. You must specify one of the following flags: 

  * `--setup-config` and optionally `--trigger-service-account`, 
  * `--redirect-traffic`, 
  * `--rollback-traffic`, 
  * `--commit` and optionally `--skip-detach`, 
  * `--abort`. 

At most one of these can be specified: 

`--abort`
     Undoes all steps of the upgrade process done so far. All traffic will point to the original 1st gen function copy and the 2nd gen function copy will be deleted. 
`--redirect-traffic`
     Redirects production traffic to the 2nd gen copy of the function. 
`--rollback-traffic`
     Rolls back production traffic to the original 1st gen copy of the function. The 2nd gen copy will still be available for testing. 
Or at least one of these can be specified: 

`--commit`
     Finishes the upgrade process and permanently deletes the original 1st gen copy of the function. 
`--skip-detach`
     The function will not be detached when committing the upgrade to allow continued use of the Cloud Functions v2 API. You can detach the function to Cloud Run afterward <https://docs.cloud.google.com/run/docs/functions/comparison#detach_your_function>. This flag is only valid when used with the --commit flag. 
Or at least one of these can be specified: 

`--max-instances`=`MAX_INSTANCES`
     Sets the maximum number of instances for the function. A function execution that would exceed max-instances times out. 
`--runtime`=`RUNTIME`
     Runtime in which to run the function. 

Required when deploying a new function; optional when updating an existing function. 

For a list of available runtimes, run `[gcloud functions runtimes list](https://docs.cloud.google.com/sdk/gcloud/reference/functions/runtimes/list)`. 

`--setup-config`
     Sets up the function upgrade config by creating a 2nd gen copy of the function's code and configuration. 
`--trigger-service-account`=`TRIGGER_SERVICE_ACCOUNT`
     The email address of the IAM service account associated with the Eventarc trigger for the function. This is used for authenticated invocation. 

If not provided, the function will use the project's default service account for Compute Engine. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud functions upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/functions/upgrade)
    
    
    [gcloud beta functions upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/beta/functions/upgrade)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
