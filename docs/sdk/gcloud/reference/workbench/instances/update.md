---
url: https://docs.cloud.google.com/sdk/gcloud/reference/workbench/instances/update/
title: gcloud workbench instances update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:14:09.274681+00:00
---

# gcloud workbench instances update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/workbench/instances/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud workbench instances update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud workbench instances update - updates a workbench instance 
SYNOPSIS
    

`gcloud workbench instances update` (`INSTANCE` : `--location`=`LOCATION`) [`--async`] [`--labels`=[`KEY`=`VALUE`,…]] [`--data-disk-resource-policies`=[`RESOURCE_POLICIES`,…] `--machine-type`=`MACHINE_TYPE` `--metadata`=[`KEY`=`VALUE`,…] `--tags`=[`TAGS`,…] `--accelerator-core-count`=`ACCELERATOR_CORE_COUNT` `--accelerator-type`=`ACCELERATOR_TYPE` [`--container-repository`=`CONTAINER_REPOSITORY` : `--container-tag`=`CONTAINER_TAG`] `--custom-gpu-driver-path`=`CUSTOM_GPU_DRIVER_PATH` `--install-gpu-driver` `--shielded-integrity-monitoring`=`SHIELDED_INTEGRITY_MONITORING` `--shielded-secure-boot`=`SHIELDED_SECURE_BOOT` `--shielded-vtpm`=`SHIELDED_VTPM`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Updates a workbench instance. 
EXAMPLES
     To update machine type for an instance, run: 
    
    
    gcloud workbench instances update example-instance --machine-type=n1-standard-8 --location=us-central1-a

To update labels for an instance, run: 
    
    
    gcloud workbench instances update example-instance --labels=k1=v1,k2=v2 --location=us-central1-a

POSITIONAL ARGUMENTS
    

Instance resource - User-defined unique name of this instance. The instance name must be 1 to 63 characters long and contain only lowercase letters, numeric characters, and dashes. The first character must be a lowercase letter and the last character cannot be a dash. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INSTANCE`
     ID of the instance or fully qualified identifier for the instance. 

To set the `instance` attribute: 

  * provide the argument `instance` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Google Cloud location of this environment <https://cloud.google.com/compute/docs/regions-zones/#locations>. 

To set the `location` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `notebooks/location`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--labels`=[`KEY`=`VALUE`,…]
     Labels to apply to this instance. These can be later modified by the setLabels method. 
Gce Setup for the instance 
Data disk configurations. 
`--data-disk-resource-policies`=[`RESOURCE_POLICIES`,…]
     Resource policies to apply to the data disk. Format: `projects/{project}/regions/{region}/resourcePolicies/{policy}`. 
`--machine-type`=`MACHINE_TYPE`
     The [Compute Engine machine type](https://cloud.google.com/sdk/gcloud/reference/compute/machine-types) of this instance. 
`--metadata`=[`KEY`=`VALUE`,…]
     Custom metadata to apply to this instance. 
`--tags`=[`TAGS`,…]
     Tags to apply to this instance. 
Accelerator configurations. 
`--accelerator-core-count`=`ACCELERATOR_CORE_COUNT`
     Count of cores of this accelerator. 
`--accelerator-type`=`ACCELERATOR_TYPE`
     Type of this accelerator. `ACCELERATOR_TYPE` must be one of: `NVIDIA_TESLA_K80`, `NVIDIA_TESLA_P100`, `NVIDIA_TESLA_V100`, `NVIDIA_TESLA_P4`, `NVIDIA_TESLA_T4`, `NVIDIA_TESLA_A100`, `NVIDIA_A100_80GB`, `NVIDIA_TESLA_T4_VWS`, `NVIDIA_TESLA_P100_VWS`, `NVIDIA_TESLA_P4_VWS`, `NVIDIA_L4`, `NVIDIA_H100_80GB`, `NVIDIA_H100_MEGA_80GB`, `NVIDIA_H200_141GB`, `NVIDIA_B200`, `NVIDIA_RTX6000`. 
Container image configurations. 
`--container-repository`=`CONTAINER_REPOSITORY`
     The path to the container image repository. For example: gcr.io/`{project_id}`/`{image_name}`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--container-tag`=`CONTAINER_TAG`
     The tag of the container image. If not specified, this defaults to the latest tag. 
GPU driver configurations. 
`--custom-gpu-driver-path`=`CUSTOM_GPU_DRIVER_PATH`
     custom gpu driver path 
`--install-gpu-driver`
     Install gpu driver 
Shielded VM configurations. 
`--shielded-integrity-monitoring`=`SHIELDED_INTEGRITY_MONITORING`
     Boolean. Enable monitoring of the boot integrity of the instance. Supported values: `true`, `false`. 
`--shielded-secure-boot`=`SHIELDED_SECURE_BOOT`
     Boolean. Boot instance with secure boot enabled. Supported values: `true`, `false`. 
`--shielded-vtpm`=`SHIELDED_VTPM`
     Boolean. Boot instance with TPM (Trusted Platform Module) enabled. Supported values: `true`, `false`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud beta workbench instances update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/workbench/instances/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-09 UTC."],[],[]] 
