---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus/tpu-vm/attach-disk/
title: gcloud alpha compute tpus tpu-vm attach-disk \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:38:23.351696+00:00
---

# gcloud alpha compute tpus tpu-vm attach-disk  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus/tpu-vm/attach-disk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute tpus tpu-vm attach-disk Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute tpus tpu-vm attach-disk - attach disk to TPU VM 
SYNOPSIS
    

`gcloud alpha compute tpus tpu-vm attach-disk` (`TPU` : `--zone`=`ZONE`) `--disk`=`DISK` [`--mode`=`MODE`; default="read-write"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute tpus tpu-vm attach-disk` is used to attach a disk to a TPU VM. For example, 
    
    
    [gcloud compute tpus tpu-vm](https://docs.cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm) attach-disk example-tpu --disk=example-disk --mode=read-only --zone=us-central1-a

attaches the disk named 'example-disk' to a TPU VM named 'example-tpu' in read-only mode in zone ``us-central1-a``. 

EXAMPLES
     To attach a disk named 'my-disk' for read-only access to a TPU named 'my-tpu', run: 
    
    
    gcloud alpha compute tpus tpu-vm attach-disk my-tpu --disk=my-disk --mode=read-only

To attach a disk named 'my-read-write-disk' for read-write access to a TPU named 'my-tpu', run: 
    
    
    gcloud alpha compute tpus tpu-vm attach-disk my-tpu --disk=my-read-write-disk

To attach a regional disk named for read-write access to a TPU named 'my-tpu', run: 
    
    
    gcloud alpha compute tpus tpu-vm attach-disk my-tpu --disk=projects/tpu-test-env-one-vm/region/us-central1/disks/example-disk

POSITIONAL ARGUMENTS
    

TPU resource - The TPU function name to attach disk. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `tpu` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`TPU`
     ID of the TPU or fully qualified identifier for the TPU. 

To set the `TPU` attribute: 

  * provide the argument `tpu` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--zone`=`ZONE`
     The Cloud zone for the TPU. 

To set the `zone` attribute: 

  * provide the argument `tpu` on the command line with a fully specified name; 
  * provide the argument `--zone` on the command line. 


REQUIRED FLAGS
    

`--disk`=`DISK`
     The name of the disk to attach to the TPU VM. 
OPTIONAL FLAGS
    

`--mode`=`MODE`; default="read-write"
     Specifies the mode of the disk. `MODE` must be one of: 

`read-only`
     Read-only. 
`read-write`
     Read-write. It is an error to attach a disk in read-write mode to more than one TPU VM. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
