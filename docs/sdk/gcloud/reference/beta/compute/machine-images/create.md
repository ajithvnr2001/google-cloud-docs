---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/machine-images/create/
title: gcloud beta compute machine-images create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:32:33.843227+00:00
---

# gcloud beta compute machine-images create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/machine-images/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute machine-images create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute machine-images create - create a Compute Engine machine image 
SYNOPSIS
    

`gcloud beta compute machine-images create` `IMAGE` `--source-instance`=`SOURCE_INSTANCE` [`--csek-key-file`=`FILE`] [`--description`=`DESCRIPTION`] [`--guest-flush`] [`--kms-key-service-account`=`KMS_KEY_SERVICE_ACCOUNT`] [`--no-require-csek-key-create`] [`--resource-manager-tags`=[`KEY`=`VALUE`,…]] [`--source-disk-csek-key`=[`PROPERTY`=`VALUE`,…]] [`--source-instance-zone`=`SOURCE_INSTANCE_ZONE`] [`--storage-location`=`LOCATION`] [`--exclude-disks`=`DISK_DEVICE_NAME`[,`DISK_DEVICE_NAME`],[…] | `--include-disks`=`DISK_DEVICE_NAME`[,`DISK_DEVICE_NAME`],[…]] [`--kms-key`=`KMS_KEY` : `--kms-keyring`=`KMS_KEYRING` `--kms-location`=`KMS_LOCATION` `--kms-project`=`KMS_PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a Compute Engine machine image. 
EXAMPLES
     To create a machine image, run: 
    
    
    gcloud beta compute machine-images create my-machine-image --source-instance=example-source --source-instance-zone=us-central1-a

POSITIONAL ARGUMENTS
    

`IMAGE`
     Name of the machineImage to create. 
REQUIRED FLAGS
    

`--source-instance`=`SOURCE_INSTANCE`
     The source instance to create a machine image from. 
OPTIONAL FLAGS
    

`--csek-key-file`=`FILE`
     (DEPRECATED) Path to a Customer-Supplied Encryption Key (CSEK) key file that maps Compute Engine machine images to user managed keys to be used when creating, mounting, or taking snapshots of disks. 
    
    
    If you pass `-` as value of the flag, the CSEK is read from stdin.
    See <https://cloud.google.com/compute/docs/disks/customer-supplied-encryption> for more details.

The --csek-key-file flag is deprecated. 

`--description`=`DESCRIPTION`
     Specifies a text description of the machine image. 
`--guest-flush`
     Create an application-consistent machine image by informing the OS to prepare for the snapshot process. 
`--kms-key-service-account`=`KMS_KEY_SERVICE_ACCOUNT`
     Service account being used for the encryption request for the given KMS key. 
`--require-csek-key-create`
     (DEPRECATED) Refuse to create machine images not protected by a user managed key in the key file when --csek-key-file is given. This behavior is enabled by default to prevent incorrect gcloud invocations from accidentally creating machine images with no user managed key. Disabling the check allows creation of some machine images without a matching Customer-Supplied Encryption Key in the supplied --csek-key-file. See <https://cloud.google.com/compute/docs/disks/customer-supplied-encryption> for more details. 

The --require-csek-key-create flag is deprecated. Enabled by default, use `--no-require-csek-key-create` to disable. 

`--resource-manager-tags`=[`KEY`=`VALUE`,…]
     A comma-separated list of Resource Manager tags to apply to the machine image. 
`--source-disk-csek-key`=[`PROPERTY`=`VALUE`,…]
     (DEPRECATED) Customer-supplied encryption key of the disk attached to the source instance. Required if the source disk is protected by a customer-supplied encryption key. This flag can be repeated to specify multiple attached disks. 
    
    
    *disk*::: URL of the disk attached to the source instance.
    This can be a full or   valid partial URL
    
    
    *csek-key-file*::: path to customer-supplied encryption key.

The --source-disk-csek-key flag is deprecated. 

`--source-instance-zone`=`SOURCE_INSTANCE_ZONE`
     Zone of the instance to operate on. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

`--storage-location`=`LOCATION`
     Google Cloud Storage location, either regional or multi-regional, where machine image's content is to be stored. If absent, a nearby regional or multi-regional location is chosen automatically. 
At most one of these can be specified: 

`--exclude-disks`=`DISK_DEVICE_NAME`[,`DISK_DEVICE_NAME`],[…]
     Specifies a filter for disks to be excluded from the machine image. The filter is a comma-separated list of disk device names. Excluding the boot disk device name is not permitted. Cannot be used in conjunction with --include-disks. 
`--include-disks`=`DISK_DEVICE_NAME`[,`DISK_DEVICE_NAME`],[…]
     Specifies a filter for disks to be included in the machine image. The filter is a comma-separated list of disk device names and must always include the boot disk's device name. Cannot be used in conjunction with --exclude-disks. 
Key resource - The Cloud KMS (Key Management Service) cryptokey that will be used to protect the machine image. The 'Compute Engine Service Agent' service account must hold permission 'Cloud KMS CryptoKey Encrypter/Decrypter'. The arguments in this group can be used to specify the attributes of this resource. 
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
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute machine-images create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/machine-images/create)
    
    
    [gcloud alpha compute machine-images create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/machine-images/create)
    
    
    [gcloud preview compute machine-images create](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/machine-images/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
