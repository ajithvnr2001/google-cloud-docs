---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/persistent-resources/create/
title: gcloud alpha ai persistent-resources create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:22:27.715093+00:00
---

# gcloud alpha ai persistent-resources create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/persistent-resources/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha ai persistent-resources create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha ai persistent-resources create - create a new persistent resource 
SYNOPSIS
    

`gcloud alpha ai persistent-resources create` `--persistent-resource-id`=`PERSISTENT_RESOURCE_ID` (`--config`=`CONFIG` `--resource-pool-spec`=[`RESOURCE_POOL_SPEC`,…]) [`--display-name`=`DISPLAY_NAME`] [`--enable-custom-service-account`] [`--labels`=[`KEY`=`VALUE`,…]] [`--network`=`NETWORK`] [`--region`=`REGION`] [`--kms-key`=`KMS_KEY` : `--kms-keyring`=`KMS_KEYRING` `--kms-location`=`KMS_LOCATION` `--kms-project`=`KMS_PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command will create a persistent resource on the users project to use with Vertex AI custom training jobs. Persistent resources remain active until they are deleted by the user. 
EXAMPLES
     To create a PersistentResource under project ``example`` in region ``us-central1``, run: 
    
    
    gcloud alpha ai persistent-resources create --region=us-central1 --project=example --resource-pool-spec=replica-count=1,machine-type='n1-standard-4' --display-name=example-resource

REQUIRED FLAGS
    

`--persistent-resource-id`=`PERSISTENT_RESOURCE_ID`
     User-specified ID of the Persistent Resource. 
resource pool specification. 

At least one of these must be specified: 

`--config`=`CONFIG`
     Path to the Persistent Resource configuration file. This file should be a YAML document containing a list of `ResourcePool` If an option is specified both in the configuration file **and** via command-line arguments, the command-line arguments override the configuration file. Note that keys with underscore are invalid. 

Example(YAML): 
    
    
    resourcePoolSpecs:
      machineSpec:
        machineType: n1-standard-4
      replicaCount: 1

`--resource-pool-spec`=[`RESOURCE_POOL_SPEC`,…]
     Defines a resource pool to be created in the Persistent Resource. You can include multiple resource pool specs in order to create a Persistent Resource with multiple resource pools. 

The spec can contain the following fields: 

`machine-type`
     (Required): The type of the machine. see <https://cloud.google.com/vertex-ai/docs/training/configure-compute#machine-types> for supported types. This field corresponds to the `machineSpec.machineType` field in `ResourcePool` API message. 
`replica-count`
     (Required if autoscaling not enabled) The number of replicas to use when creating this resource pool. This field corresponds to the replicaCount field in 'ResourcePool' API message. 
`min-replica-count`
     (Optional) The minimum number of replicas that autoscaling will down-size to for this resource pool. Both min-replica-count and max-replica-count are required to enable autoscaling on this resource pool. The value for this parameter must be at least 1. 
`max-replica-count`
     (Optional) The maximum number of replicas that autoscaling will create for this resource pool. Both min-replica-count and max-replica-count are required to enable autoscaling on this resource pool. The maximum value for this parameter is 1000. 
`accelerator-type`
     (Optional) The type of GPU to attach to the machines. see <https://cloud.google.com/vertex-ai/docs/training/configure-compute#specifying_gpus> for more requirements. This field corresponds to the `machineSpec.acceleratorType` field in `ResourcePool` API message. 
`accelerator-count`
     (Required with accelerator-type) The number of GPUs for each VM in the resource pool to use. The default the value if 1. This field corresponds to the `machineSpec.acceleratorCount` field in `ResourcePool` API message. 
`disk-type`
     (Optional) The type of disk to use for each machine's boot disk in the resource pool. The default is `pd-standard`. This field corresponds to the `diskSpec.bootDiskType` field in `ResourcePool` API message. 
`disk-size`
     (Optional) The disk size in Gb for each machine's boot disk in the resource pool. The default is `100`. This field corresponds to the `diskSpec.bootDiskSizeGb` field in `ResourcePool` API message. 
Example: --worker-pool-spec=replica-count=1,machine-type=n1-highmem-2 
OPTIONAL FLAGS
    

`--display-name`=`DISPLAY_NAME`
     Display name of the Persistent Resource. 
`--enable-custom-service-account`
     Whether or not to use a custom user-managed service account with this Persistent Resource. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--network`=`NETWORK`
     Full name of the Google Compute Engine network to which the Job is peered with. Private services access must already have been configured. If unspecified, the Job is not peered with any network. 
Region resource - Cloud region to create a Persistent Resource. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--region` on the command line with a fully specified name; 
  * set the property `ai/region` with a fully specified name; 
  * choose one from the prompted list of available regions with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--region`=`REGION`
     ID of the region or fully qualified identifier for the region. 

To set the `region` attribute: 

  * provide the argument `--region` on the command line; 
  * set the property `ai/region`; 
  * choose one from the prompted list of available regions. 


Key resource - The Cloud KMS (Key Management Service) cryptokey that will be used to protect the persistent resource. The 'Vertex AI Service Agent' service account must hold permission 'Cloud KMS CryptoKey Encrypter/Decrypter'. The arguments in this group can be used to specify the attributes of this resource. 
`--kms-key`=`KMS_KEY`
     ID of the key or fully qualified identifier for the key. 

To set the `kms-key` attribute: 

  * provide the argument `--kms-key` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--kms-keyring`=`KMS_KEYRING`
     The KMS keyring of the key. 

To set the `kms-keyring` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-keyring` on the command line. 


`--kms-location`=`KMS_LOCATION`
     The Google Cloud location for the key. 

To set the `kms-location` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-location` on the command line. 


`--kms-project`=`KMS_PROJECT`
     The Google Cloud project for the key. 

To set the `kms-project` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-project` on the command line; 
  * set the property `core/project`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud ai persistent-resources create](https://docs.cloud.google.com/sdk/gcloud/reference/ai/persistent-resources/create)
    
    
    [gcloud beta ai persistent-resources create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/persistent-resources/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
