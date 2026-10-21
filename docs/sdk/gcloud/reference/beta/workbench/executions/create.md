---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/workbench/executions/create/
title: gcloud beta workbench executions create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:35:03.358697+00:00
---

# gcloud beta workbench executions create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/workbench/executions/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta workbench executions create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta workbench executions create - create a Workbench execution 
SYNOPSIS
    

`gcloud beta workbench executions create` `--region`=`REGION` (`--display-name`=`DISPLAY_NAME` `--gcs-output-uri`=`GCS_OUTPUT_URI` `--service-account`=`SERVICE_ACCOUNT` (`--direct-content`=`DIRECT_CONTENT` | [`--gcs-notebook-uri`=`GCS_NOTEBOOK_URI` : `--generation`=`GENERATION`]) : `--execution-timeout`=`EXECUTION_TIMEOUT`; default="24h" `--kernel-name`=`KERNEL_NAME`; default="python3" `--accelerator-count`=`ACCELERATOR_COUNT` `--accelerator-type`=`ACCELERATOR_TYPE` `--machine-type`=`MACHINE_TYPE`; default="e2-standard-4" `--disk-size-gb`=`DISK_SIZE_GB`; default=100 `--disk-type`=`DISK_TYPE` `--no-enable-internet-access` `--network`=`NETWORK` [`--subnetwork`=`SUBNETWORK` : `--subnetwork-region`=`SUBNETWORK_REGION`] [`--kms-key`=`KMS_KEY` : `--kms-keyring`=`KMS_KEYRING` `--kms-location`=`KMS_LOCATION` `--kms-project`=`KMS_PROJECT`]) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a Workbench notebook execution. 
EXAMPLES
     To create an execution of a notebook file with Cloud Storage URI `gs://my-bucket/my-notebook.ipynb`, with an execution job display name `my-execution`, running with service account `my-service-account@my-project.iam.gserviceaccount.com`, with results uploaded to Cloud Storage bucket `gs://my-bucket/results`, and in region `us-central1`, with a compute configuration of `n1-standard-4` machine type: 
    
    
    gcloud beta workbench executions create --display-name=my-execution --gcs-notebook-uri=gs://my-bucket/my-notebook.ipynb --service-account=my-service-account@my-project.iam.gserviceaccount.com --gcs-output-uri=gs://my-bucket/results --region=us-central1 --machine-type=n1-standard-4

REQUIRED FLAGS
    

Region resource - Cloud region to create. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--region` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--region`=`REGION`
     ID of the region or fully qualified identifier for the region. 

To set the `region` attribute: 

  * provide the argument `--region` on the command line. 


Configuration of the execution job. 

This must be specified. 

`--display-name`=`DISPLAY_NAME`
     The display name of the execution. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--gcs-output-uri`=`GCS_OUTPUT_URI`
     The Cloud Storage location to upload notebook execution results to. Format: gs://bucket-name. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--service-account`=`SERVICE_ACCOUNT`
     The service account to run the execution as 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--execution-timeout`=`EXECUTION_TIMEOUT`; default="24h"
     The max running time of the execution job, as a duration. See '$ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)' for details on formatting the input duration. 
`--kernel-name`=`KERNEL_NAME`; default="python3"
     The kernel name to use for the execution. 
Source of the notebook to execute. 

Exactly one of these must be specified: 

`--direct-content`=`DIRECT_CONTENT`
     The direct notebook content as IPYNB. This can be a local filepath to an .ipynb file or can be set to `-` to read content from stdin. 
Or at least one of these can be specified: 

The Cloud Storage notebook source. 
`--gcs-notebook-uri`=`GCS_NOTEBOOK_URI`
     The Cloud Storage uri pointing to the notebook. Format: gs://bucket/notebook_file.ipynb 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--generation`=`GENERATION`
     The version of the Cloud Storage object to read. If unset, the current version of the object will be used. 
Compute configuration of the execution job. 
The machine configuration of the runtime. 
`--accelerator-count`=`ACCELERATOR_COUNT`
     The number of accelerators used by the runtime. 
`--accelerator-type`=`ACCELERATOR_TYPE`
     The type of hardware accelerator used by the runtime. If specified, \--accelerator-count must also be specified. `ACCELERATOR_TYPE` must be one of: `NVIDIA_TESLA_V100`, `NVIDIA_TESLA_T4`, `NVIDIA_TESLA_A100`, `NVIDIA_A100_80GB`, `NVIDIA_L4`. 
`--machine-type`=`MACHINE_TYPE`; default="e2-standard-4"
     The Compute Engine machine type selected for the runtime. 
The configuration for the data disk of the runtime. 
`--disk-size-gb`=`DISK_SIZE_GB`; default=100
     The disk size of the runtime in GB. If specified, the --disk-type must also be specified. The minimum size is 10GB and the maximum is 65536GB. 
`--disk-type`=`DISK_TYPE`
     The type of the disk. `DISK_TYPE` must be one of: `PD_STANDARD`, `PD_SSD`, `PD_BALANCED`, `PD_EXTREME`, `HYPERDISK_BALANCED`. 
The network configuration for the runtime. 
`--enable-internet-access`
     Enable public internet access for the runtime. Enabled by default, use `--no-enable-internet-access` to disable. 
Network resource - The name of the VPC that this runtime is in. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--network` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--network`=`NETWORK`
     ID of the network or fully qualified identifier for the network. 

To set the `network` attribute: 

  * provide the argument `--network` on the command line. 


Subnetwork resource - The name of the subnetwork that this runtime is in. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--subnetwork` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--subnetwork`=`SUBNETWORK`
     ID of the subnetwork or fully qualified identifier for the subnetwork. 

To set the `subnetwork` attribute: 

  * provide the argument `--subnetwork` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--subnetwork-region`=`SUBNETWORK_REGION`
     Google Cloud region of this subnetwork <https://cloud.google.com/compute/docs/regions-zones/#locations>. 

To set the `subnetwork-region` attribute: 

  * provide the argument `--subnetwork` on the command line with a fully specified name; 
  * provide the argument `--subnetwork-region` on the command line. 


Key resource - The Cloud KMS encryption key (customer-managed encryption key) used to protect the execution. The key must be in the same region as the execution. If not specified, Google-managed encryption will be used. The arguments in this group can be used to specify the attributes of this resource. 
`--kms-key`=`KMS_KEY`
     ID of the key or fully qualified identifier for the key. 

To set the `kms-key` attribute: 

  * provide the argument `--kms-key` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--kms-keyring`=`KMS_KEYRING`
     KMS keyring id of the key. 

To set the `kms-keyring` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-keyring` on the command line. 


`--kms-location`=`KMS_LOCATION`
     Cloud location for the key. 

To set the `kms-location` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-location` on the command line. 


`--kms-project`=`KMS_PROJECT`
     Cloud project id for the key. 

To set the `kms-project` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-project` on the command line. 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud workbench executions create](https://docs.cloud.google.com/sdk/gcloud/reference/workbench/executions/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
