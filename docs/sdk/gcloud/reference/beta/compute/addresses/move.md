---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/addresses/move/
title: gcloud beta compute addresses move \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:25.063190+00:00
---

# gcloud beta compute addresses move  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/addresses/move/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute addresses move Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute addresses move - move an address to another project 
SYNOPSIS
    

`gcloud beta compute addresses move` `NAME` `--target-project`=`TARGET_PROJECT` [`--description`=`DESCRIPTION`] [`--new-name`=`NEW_NAME`] [`--global` | `--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     The following command moves address `external-ip1` in region `us-central1` to project `test-playground` with new address name `test-ip1`: 
    
    
    gcloud beta compute addresses move external-ip1 --new-name=test-ip1 --target-project=test-playground --region=us-central1

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the address to operate on. 
REQUIRED FLAGS
    

`--target-project`=`TARGET_PROJECT`
     The target project to move address to. It can be either a project name or a project numerical ID. It must not be the same as the current project. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     Description of moved new address. 
`--new-name`=`NEW_NAME`
     Name of moved new address. If not specified, current address's name is used. 
At most one of these can be specified: 

`--global`
     If set, the address is global. 
`--region`=`REGION`
     Region of the address to operate on. Overrides the default `compute/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute addresses move](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/move)
    
    
    [gcloud alpha compute addresses move](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/move)
    
    
    [gcloud preview compute addresses move](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/addresses/move)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
