---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/suspend/
title: gcloud beta compute instances suspend \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:12:37.197435+00:00
---

# gcloud beta compute instances suspend  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/suspend/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute instances suspend Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute instances suspend - suspend a virtual machine instance 
SYNOPSIS
    

`gcloud beta compute instances suspend` `INSTANCE_NAMES` [`INSTANCE_NAMES` …] [`--async`] [`--discard-local-ssd`[=`DISCARD_LOCAL_SSD`]] [`--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute instances suspend` is used to suspend a Compute Engine virtual machine. Suspending a VM is the equivalent of sleep or standby mode: the guest receives an ACPI S3 suspend signal, after which all VM state is saved to temporary storage. An instance can only be suspended while it is in the RUNNING state. A suspended instance will be put in SUSPENDED state. 

Note: A suspended instance can be resumed by running the gcloud compute instances resume command. 

If a VM has any attached Local SSD disks, you can preserve the Local SSD data when you suspend the VM by setting `--discard-local-ssd=False`. Preserving the Local SSD disk data incurs costs and is subject to limitations. 

Limitations: 

  * Limitations for suspending a VM: <https://cloud.google.com/compute/docs/instances/suspend-resume-instance#limitations>
  * Limitations for preserving Local SSD data: <https://cloud.google.com/compute/docs/disks/local-ssd#stop_instance>


EXAMPLES
     To suspend an instance named ``test-instance``, run: 
    
    
    gcloud beta compute instances suspend test-instance

To suspend an instance named `test-instance` that has a Local SSD, run: 
    
    
    gcloud beta compute instances suspend test-instance --discard-local-ssd=True

Using `--discard-local-ssd` without a value defaults to `True`. 

POSITIONAL ARGUMENTS
    

`INSTANCE_NAMES` [`INSTANCE_NAMES` …]
     Names of the instances to operate on. For details on valid instance names, refer to the criteria documented under the field 'name' at: <https://cloud.google.com/compute/docs/reference/rest/v1/instances>
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--discard-local-ssd`[=`DISCARD_LOCAL_SSD`]
     If set to true, local SSD data is discarded. 
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
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute instances suspend](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/suspend)
    
    
    [gcloud alpha compute instances suspend](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/suspend)
    
    
    [gcloud preview compute instances suspend](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/suspend)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
