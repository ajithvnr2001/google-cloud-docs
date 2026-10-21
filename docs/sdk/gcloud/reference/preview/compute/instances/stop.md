---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/stop/
title: gcloud preview compute instances stop \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:36:14.986289+00:00
---

# gcloud preview compute instances stop  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/stop/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute instances stop Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute instances stop - stop a virtual machine instance 
SYNOPSIS
    

`gcloud preview compute instances stop` `INSTANCE_NAMES` [`INSTANCE_NAMES` …] [`--async`] [`--discard-local-ssd`[=`DISCARD_LOCAL_SSD`]] [`--no-graceful-shutdown`] [`--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute instances stop` is used to stop a Compute Engine virtual machine. Stopping a VM performs a clean shutdown, much like invoking the shutdown functionality of a workstation or laptop. 

If a VM has any attached Local SSD disks, you must use the `--discard-local-ssd` flag to indicate whether or not the Local SSD data should be discarded. To stop the VM and preserve the Local SSD data when you stop the VM by setting `--discard-local-ssd=False`. 

To stop the VM and discard the Local SSD data, specify `--discard-local-ssd=True`. 

Preserving the Local SSD disk data incurs costs and is subject to limitations. See <https://cloud.google.com/compute/docs/disks/local-ssd#stop_instance> for more information. 

Stopping a VM which is already stopped will return without errors. 

EXAMPLES
     To stop an instance named `test-instance`, run: 
    
    
    gcloud preview compute instances stop test-instance

To stop an instance named `test-instance` that has a Local SSD, run: 
    
    
    gcloud preview compute instances stop test-instance --discard-local-ssd=True

Using '--discard-local-ssd' without a value defaults to True. 

POSITIONAL ARGUMENTS
    

`INSTANCE_NAMES` [`INSTANCE_NAMES` …]
     Names of the instances to operate on. For details on valid instance names, refer to the criteria documented under the field 'name' at: <https://cloud.google.com/compute/docs/reference/rest/v1/instances>
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--discard-local-ssd`[=`DISCARD_LOCAL_SSD`]
     If set to true, local SSD data is discarded. 
`--no-graceful-shutdown`
     Stops the instance immediately without gracefully shutting it down. If a graceful shutdown is in progress, then the instance is forcefully stopped. 
`--zone`=`ZONE`
     Zone of the instances to operate on. If not specified, you might be prompted to select a zone (interactive mode only). `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` attempts to identify the appropriate zone by searching for resources in your currently active project. If the zone cannot be determined, `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with all available Google Cloud Platform zones. 

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
    
    
    [gcloud compute instances stop](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/stop)
    
    
    [gcloud alpha compute instances stop](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/stop)
    
    
    [gcloud beta compute instances stop](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/stop)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
