---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/instances/enable-debug/
title: gcloud beta app instances enable-debug \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:13:58.066300+00:00
---

# gcloud beta app instances enable-debug  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/instances/enable-debug/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app instances enable-debug Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app instances enable-debug - enable debug mode for an instance (only works on the flexible environment)
SYNOPSIS
    

`gcloud beta app instances enable-debug` [`INSTANCE`] [`--service`=`SERVICE`, `-s` `SERVICE`] [`--version`=`VERSION`, `-v` `VERSION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` When in debug mode, SSH will be enabled on the VMs, and you can use `[gcloud compute ssh](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh)` to login to them. They will be removed from the health checking pools, but they still receive requests. 

Note that any local changes to an instance will be `lost` if debug mode is disabled on the instance. New instance(s) may spawn depending on the app's scaling settings. 

Additionally, debug mode doesn't work for applications using the App Engine standard environment. 

EXAMPLES
     To enable debug mode for a particular instance, run: 
    
    
    gcloud beta app instances enable-debug --service=s1 --version=v1 i1

To enable debug mode for an instance chosen interactively, run: 
    
    
    gcloud beta app instances enable-debug

POSITIONAL ARGUMENTS
    

[`INSTANCE`]
     Instance ID to enable debug mode on. If not specified, select instance interactively. Must uniquely specify (with other flags) exactly one instance 
FLAGS
    

`--service`=`SERVICE`, `-s` `SERVICE`
     If specified, only match instances belonging to the given service. This affects both interactive and non-interactive selection. 
`--version`=`VERSION`, `-v` `VERSION`
     If specified, only match instances belonging to the given version. This affects both interactive and non-interactive selection. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud app instances enable-debug](https://docs.cloud.google.com/sdk/gcloud/reference/app/instances/enable-debug)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
