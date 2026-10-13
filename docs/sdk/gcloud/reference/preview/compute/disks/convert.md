---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/disks/convert/
title: gcloud preview compute disks convert \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:51.320792+00:00
---

# gcloud preview compute disks convert  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/disks/convert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute disks convert Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute disks convert - convert a Compute Engine Persistent Disk volume to a Hyperdisk volume 
SYNOPSIS
    

`gcloud preview compute disks convert` `DISK_NAME` `--target-disk-type`=`TARGET_DISK_TYPE` [`--kms-key`=`KMS_KEY` : `--kms-keyring`=`KMS_KEYRING` `--kms-location`=`KMS_LOCATION` `--kms-project`=`KMS_PROJECT`] [`--region`=`REGION` | `--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` Convert Compute Engine Persistent Disk volumes to Hyperdisk volumes. 

`gcloud preview compute disks convert` converts a Compute Engine Persistent Disk volume to a Hyperdisk volume. For a comprehensive guide, refer to: <https://cloud.google.com/sdk/gcloud/reference/compute/disks/convert>. 

EXAMPLES
     The following command converts a Persistent Disk volume to a Hyperdisk Balanced volume: 
    
    
    gcloud preview compute disks convert my-disk-1 --zone=ZONE --target-disk-type=hyperdisk-balanced

POSITIONAL ARGUMENTS
    

`DISK_NAME`
     Name of the disk to operate on. 
REQUIRED FLAGS
    

`--target-disk-type`=`TARGET_DISK_TYPE`
     Specifies the type of Hyperdisk to convert to, for example, to convert a Hyperdisk Balanced volume, specify `hyperdisk-balanced`. To get a list of available disk types, run `[gcloud compute disk-types list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disk-types/list)`. 
OPTIONAL FLAGS
    

Key resource - The Cloud KMS (Key Management Service) cryptokey that will be used to protect the disk. The 'Compute Engine Service Agent' service account must hold permission 'Cloud KMS CryptoKey Encrypter/Decrypter'. The arguments in this group can be used to specify the attributes of this resource. 
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
  * provide the argument `--kms-location` on the command line; 
  * provide the argument `--region` on the command line. 


`--kms-project`=`KMS_PROJECT`
     The Google Cloud project for the key. 

To set the `kms-project` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-project` on the command line; 
  * set the property `core/project`. 


At most one of these can be specified: 

`--region`=`REGION`
     Region of the disk to operate on. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--zone`=`ZONE`
     Zone of the disk to operate on. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
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
    
    
    [gcloud compute disks convert](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/convert)
    
    
    [gcloud alpha compute disks convert](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/convert)
    
    
    [gcloud beta compute disks convert](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/disks/convert)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
