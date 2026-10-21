---
url: https://docs.cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create/
title: gcloud colab runtime-templates create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:19:40.144861+00:00
---

# gcloud colab runtime-templates create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud colab runtime-templates create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud colab runtime-templates create - create a runtime template 
SYNOPSIS
    

`gcloud colab runtime-templates create` `--display-name`=`DISPLAY_NAME` [`--async`] [`--region`=`REGION`] [`--runtime-template-id`=`RUNTIME_TEMPLATE_ID`] [`--description`=`DESCRIPTION` `--no-enable-euc` `--enable-secure-boot` `--idle-shutdown-timeout`=`IDLE_SHUTDOWN_TIMEOUT`; default="3h" `--labels`=[`KEY`=`VALUE`,…] `--network-tags`=[`TAGS`,…] `--accelerator-count`=`ACCELERATOR_COUNT` `--accelerator-type`=`ACCELERATOR_TYPE` `--machine-type`=`MACHINE_TYPE`; default="e2-standard-4" `--disk-size-gb`=`DISK_SIZE_GB`; default=100 `--disk-type`=`DISK_TYPE` [`--kms-key`=`KMS_KEY` : `--kms-keyring`=`KMS_KEYRING` `--kms-location`=`KMS_LOCATION` `--kms-project`=`KMS_PROJECT`] `--no-enable-internet-access` `--network`=`NETWORK` [`--subnetwork`=`SUBNETWORK` : `--subnetwork-region`=`SUBNETWORK_REGION`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a Colab Enterprise runtime template, a VM configuration for your notebook runtimes. 
EXAMPLES
     To create a runtime template in region 'us-central1' with the display name 'my-runtime-template', run: 
    
    
    gcloud colab runtime-templates create --region=us-central1 --display-name=my-runtime-template

To create a runtime template for a VM with machine type n1-standard-2 and one NVIDIA_TESLA_V100 accelerator, run: 
    
    
    gcloud colab runtime-templates create --machine-type=n1-standard-2 --accelerator-type=NVIDIA_TESLA_V100 --accelerator-count=1 --region=us-central1 --display-name=my-runtime-template

To create a runtime template that disables end user credential access, run: 
    
    
    gcloud colab runtime-templates create --no-enable-euc --region=us-central1 --display-name=my-runtime-template

REQUIRED FLAGS
    

`--display-name`=`DISPLAY_NAME`
     The display name of the runtime template. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
Region resource - Cloud region to create runtime template. Please see <https://cloud.google.com/colab/docs/locations> for a list of supported regions. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--region` on the command line with a fully specified name; 
  * set the property `colab/region` with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--region`=`REGION`
     ID of the region or fully qualified identifier for the region. 

To set the `region` attribute: 

  * provide the argument `--region` on the command line; 
  * set the property `colab/region`. 


`--runtime-template-id`=`RUNTIME_TEMPLATE_ID`
     The id of the runtime template. If not specified, a random id will be generated. 
Configuration of the runtime template 
`--description`=`DESCRIPTION`
     The description of the runtime template. 
`--enable-euc`
     Enable end user credential access for the runtime. Enabled by default, use `--no-enable-euc` to disable. 
`--enable-secure-boot`
     Enables secure boot for the runtime. Disabled by default. 
`--idle-shutdown-timeout`=`IDLE_SHUTDOWN_TIMEOUT`; default="3h"
     The duration after which the runtime is automatically shut down. An input of 0s disables the idle shutdown feature, and a valid range is [10m, 24h]. See '$ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)' for details on formatting the input duration. 
`--labels`=[`KEY`=`VALUE`,…]
     Add labels to identify and group the runtime template. 
`--network-tags`=[`TAGS`,…]
     Applies the given Compute Engine tags to the runtime. 
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
Key resource - The Cloud KMS encryption key (customer-managed encryption key) used to protect the runtime. The key must be in the same region as the runtime. If not specified, Google-managed encryption keys will be used. The arguments in this group can be used to specify the attributes of this resource. 
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


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud beta colab runtime-templates create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/colab/runtime-templates/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
