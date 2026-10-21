---
url: https://docs.cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/create/
title: gcloud notebooks runtimes create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:16:43.621254+00:00
---

# gcloud notebooks runtimes create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud notebooks runtimes create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud notebooks runtimes create - request for creating an runtime 
SYNOPSIS
    

`gcloud notebooks runtimes create` (`RUNTIME` : `--location`=`LOCATION`) (`--runtime-access-type`=`RUNTIME_ACCESS_TYPE` `--runtime-owner`=`RUNTIME_OWNER`) (`--runtime-type`=`RUNTIME_TYPE` | [`--machine-type`=`MACHINE_TYPE` : `--interface`=`INTERFACE` `--mode`=`MODE` `--source`=`SOURCE` `--type`=`TYPE`]) [`--async`] [`--custom-gpu-driver-path`=`CUSTOM_GPU_DRIVER_PATH` `--idle-shutdown-timeout`=`IDLE_SHUTDOWN_TIMEOUT` `--install-gpu-driver`=`INSTALL_GPU_DRIVER` `--post-startup-script`=`POST_STARTUP_SCRIPT` `--post-startup-script-behavior`=`POST_STARTUP_SCRIPT_BEHAVIOR`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Request for creating notebook runtimes. 
EXAMPLES
     To create a runtime, run: 
    
    
    gcloud notebooks runtimes create example-runtime --runtime-access-type=SINGLE_USER --runtime-owner=example@google.com --machine-type=n1-standard-4 --location=us-central1

POSITIONAL ARGUMENTS
    

Runtime resource - User-defined unique name of this runtime. The runtime name must be 1 to 63 characters long and contain only lowercase letters, numeric characters, and dashes. The first character must be a lowercase letter and the last character cannot be a dash. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `runtime` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`RUNTIME`
     ID of the runtime or fully qualified identifier for the runtime. 

To set the `runtime` attribute: 

  * provide the argument `runtime` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Google Cloud location of this runtime <https://cloud.google.com/compute/docs/regions-zones/#locations>. 

To set the `location` attribute: 

  * provide the argument `runtime` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `notebooks/location`. 


REQUIRED FLAGS
    

At least one of these must be specified: 

`--runtime-access-type`=`RUNTIME_ACCESS_TYPE`
     access type 
`--runtime-owner`=`RUNTIME_OWNER`
     runtime owner 
Exactly one of these must be specified: 

`--runtime-type`=`RUNTIME_TYPE`
     runtime type 
Or at least one of these can be specified: 

`--machine-type`=`MACHINE_TYPE`
     machine type 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--interface`=`INTERFACE`
     runtime interface 
`--mode`=`MODE`
     runtime mode 
`--source`=`SOURCE`
     runtime source 
`--type`=`TYPE`
     runtime type 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--custom-gpu-driver-path`=`CUSTOM_GPU_DRIVER_PATH`
     custom gpu driver path 
`--idle-shutdown-timeout`=`IDLE_SHUTDOWN_TIMEOUT`
     idle shutdown timeout 
`--install-gpu-driver`=`INSTALL_GPU_DRIVER`
     install gpu driver 
`--post-startup-script`=`POST_STARTUP_SCRIPT`
     post startup script 
`--post-startup-script-behavior`=`POST_STARTUP_SCRIPT_BEHAVIOR`
     post startup script behavior 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
